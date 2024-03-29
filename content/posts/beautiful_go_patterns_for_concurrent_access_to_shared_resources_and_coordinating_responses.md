+++
title = "Beautiful Go patterns for concurrent access to shared resources and coordinating responses"
date = "2014-07-26T13:22:32-04:00"
tags = ["golang"]
guid = "beautiful_go_patterns_for_concurrent_access_to_shared_resources_and_coordinating_responses"
+++

It's a pretty common thing in backend go programs to have multiple coroutines concurrently needing to modify a shared resource,
and needing a response that tells them whether the operation succeeded and/or other auxiliary information.
Something centralized manages the shared state, the changes to it and the responses.

<!--more-->

This is effectively two things.

### Pattern one: making access to thread-unsafe data structures thread safe

Making modifications to thread-unsafe data (remember, maps for example are not thread safe in go) in a thread safe way, you can use a select loop that reads
from various channels and enforces that all operations are executed serially, because only one select case can happen at the same time.
I saw this first in <a href="https://github.com/bitly/statsdaemon/blob/master/statsdaemon.go#L90">bitly's statsdaemon</a> and have since used this in various places, including <a href="https://github.com/vimeo/statsdaemon">vimeo/statsdaemon</a> and <a href="https://github.com/graphite-ng/carbon-relay-ng">carbon-relay-ng</a>, for example to route metrics (which needs read access to the routes map) while allowing changes to the routes (coming from the telnet admin interface), by having those as two cases in a select statement.  This was my first "aha!" moment.

### pattern two: coordinating flow of responses

For the second, after (potentially time consuming) work, returning a response to the invoker, (let's say in the carbon-relay-ng case where you want to notify whether the route change succeeded) I have so far just passed on references to the admin interface session along with the request, and after completion of the work it would spawn a new goroutine that resumes the session with the given response.  Not the most elegant, but it works.

The other day though, I saw a very interesting pattern for this case. I don't remember where (probably one of the gophercon presentations)
or what it's called. 
But the idea is you can simply use one shared channel for all requests, and one shared channel for all responses.
As long as the requesters write a request to the requests channel and then read a response from the other channel, and the coordinator first reads a request and then writes the response, no further synchronization is needed.  Here's a demo program:

{{< highlight go >}}
package main

// demo the fact that we can just use one shared req and one resp channel.
// as long as they are unbuffered, the synchronization works just fine.

import "fmt"
import "sync"
import "math/rand"
import "time"

var requests = make(chan int)
var responses = make(chan string)

func routine(num int, wg *sync.WaitGroup) {
    // pretend this is a routine that's doing something, like serving a user session
    // but then we need to modify some shared state
    time.Sleep(time.Duration(rand.Intn(100)) * time.Millisecond)
    requests <- num
    resp := <-responses
    fmt.Printf("routine %d gets response: %s\n", num, resp)
    wg.Done()
}

func coordinator() {
    for {
        req := <-requests
        // in here, you can do whatever modifications to shared state you need.
        time.Sleep(time.Duration(rand.Intn(100)) * time.Millisecond) // simulate some heavy lifting
        responses <- fmt.Sprintf("this return value is meant for routine %d", req)
    }
}

func main() {
    go coordinator()

    var wg sync.WaitGroup
    for i := 0; i < 10; i++ {
        wg.Add(1)
        go routine(i, &wg)
    }
    wg.Wait()
    close(requests)
}
{{< /highlight >}}

[code on Go playground](http://play.golang.org/p/32BSXT0xhN)


At first glance, it looked as if the seemingly arbitrary reading and writing from/to channels without explicit synchronization would introduce race conditions, with routines getting
the response meant for other routines.  But after some reasoning, it becomes apparent that 
the "channel operation as synchronization" keeps everything under control, in a pretty elegant way.
**There is nothing explicit to assure the routines get their response, and not the response meant for another routine.
Instead, it just flows naturally and implicitly from the ordering of the blocked channel operations.**
Another "aha!" moment for me.  I've heard "use channel operations for synchronization" often enough, and this is the most
beautiful example of it I've come across so far.  The routines are blocked on channel reads and writes, but when a channel operation occurs, that's where the respective goroutines unblock, and everything just works the way it's supposed to.  How elegant!

### Conclusion

Maybe these patterns are obvious to you, maybe they are widely known patterns.
But I think as you evolve from go rookie to experienced developer (and often need to wrap your head around new concepts and approaches)
you will encounter some interesting patterns and also have your "aha!" moments, so I hope this will help someone.

I've been using the first pattern in a few places, I haven't used the second one yet, but I know some places where I can apply it and simplify some code.
Take for example this [pull request to add a web UI to carbon-relay-ng](https://github.com/graphite-ng/carbon-relay-ng/pull/7), now the metrics-router, the admin telnet interface, **and** the new http interface will all need access to the routes map.  I'm looking forward to implement the second pattern, simplifying the code while making it more generic at the same time.

