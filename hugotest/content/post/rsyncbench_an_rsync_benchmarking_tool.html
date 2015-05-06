+++
title = "Rsyncbench, an rsync benchmarking tool"
date = "2010-10-15T09:38:12-04:00"
tags = ["foss", "perf"]
+++
<p>Background info:<br />

I'm currently in the process of evaluating (V)PS hosting providers and backup solutions.  The idea being: I want a (V)PS to run my stuff, which doesn't need much disk space,<br />

but in the meantime it might be a good idea to look for online backup solutions (oops did I say "online"? I meant "cloud"), like on the (V)PS itself, or maybe as a separate solution.<br />

But I've got some diverse amount of data (my personal data is mostly a lot of small plaintext files, my mom has a windows VM for which I considered syncing the entire vdi file)<br />

At this point the biggest contenders are <a href="http://linode.com/">Linode</a> (which offers quite some flexibility and management tools, but becomes expensive when you want extra disk space (2$/month*GB), <a href="http://www.rackspace.com/apps/backup_and_collaboration/data_backup_software/">Rackspace backup</a> gives you 10GB for 5$/month, but they have nice backup tools so I could only backup the important files from within the windows VM (~200MB), and then there's <a href="http://www.hetzner.de/">Hetzner</a>, which offers powerful physical private servers with a lot of storage (160GB) for 29eur/month, but less flexibility (I.e. kvm-over-ip costs an extra 15eur/month)</p>

<p>Another issue, given the limited capacity of Belgian internet connections, I needed to figure out how much bandwith rsync really needs, so I can calculate if the duration of a backup run including syncing the full vdi file is still reasonable.</p>

<p>I couldn't find an rsync benchmarking tool, so I wrote my own.</p>

<p>Features:</p>

<ul>

<li>simple</li>

<li>non invasive: you specify the target and destination hosts (just localhost is fine too), and file locations</li>

<li>measures time spent, bytes sent (measured with tcpdump), and data sent (rsync's statistics which takes compression into account)</li>

<li>supports plugins</li>

<li>generates png graphs using Gnuplot</li>

<li>two current plugins: one using files of various sizes, both randomly generated (/dev/urandom) and easily compressable (/dev/zero), does some use cases like initial sync, second sync (no-op), and syncing with a data block appended and prepended.  The other plugin collects vdi files from rsnapshot directories and measures the rsyncing from each image to the next</li>

</ul>

<p><!--more--><br />

Non-features:</p>

<ul>

<li>no plugins yet for other use cases then my own (no file removal, renaming, working with multiple files, working with small files, ...)</li>

<li>doesn't test a lot of different file sizes and such</li>

<li>not as finished as my other projects (no Makefile, graphs are rough.  but I have no time to go dive further in the gnuplot stuff)

<li>the benchmarking process takes a long time, due to a lot of juggling with big files. some steps can be optimized</li>

</ul>

<p>Here is an example graph:<br />

<img src="/files/rsyncbench_random_images_sent.png"/><br />

The first entry on the x-asis is on 1MiB, even though it seems like 0MiB because of the scale.<br />

Notice how rsync is pretty efficient when it has nothing to do (no-op), and the sizes of transmitted data correspond exactly to what has changed (even if you prepend data in the beginning and all data "moves to the back", rsync notices this)<br />

The compressed numbers (reported by rsync) are very close to the real numbers measured with tcpdump.  Which makes sense, random data is not easy to compress.  OTOH, if i take the graph of the case where I sync images which are built from /dev/zero, the story similar so either rsyncs compression sucks (which I find hard to believe), or the guy on #rsync who told me those numbers are about the compressed data was wrong (maybe) or I just messed up something (likely)</p>

<p>So, I hope this is useful to someone, and maybe others can clone the project and improve it further.  I found it weird that I couldn't find an rsync benchmarking tool, because rsync's algorithm is non-obvious and it can be really interesting to understand all its characteristics in various use cases.</p>

<p>Project page: <a href="http://github.com/Dieterbe/rsyncbench">rsyncbench on Github</a></p>

<p>Oh and about my backups? Rsyncing the different vdi files takes upto a few hundreds of MB's, not an ideal solution given the upload speeds in Belgium.<br />

I'll figure out something else.  Like backing up from inside windows (maybe using the rackspace service), or mounting the vdi and rsyncing the data from there.</p>
