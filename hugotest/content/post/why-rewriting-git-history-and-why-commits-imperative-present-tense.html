+++
title = "Why rewriting git history? And why should commits be in imperative present tense?"
date = "2011-03-05T18:27:35-04:00"
tags = ["foss", "git"]
+++
<p>

There are tons of articles describing <em>how</em> you can rewrite history with git, but they do not answer "<em>why</em> should I do it?".

A similar question is "what are the tradeoffs / how do I apply this in my distributed workflow?".

<br/>Also, git developers strongly encourage/command you to write commit message in imperative present tense, but do not say why.  So, why?

<br/>I'll try to answer these to the best of my abilities, largely based on how I see things.  I won't get too detailed (there are enough manuals and tutorials for the exact concepts and commands).

<!--more-->

<h3>Why rewriting git history?</h3>

<p>

Just like source code git history gets mostly read and relatively infrequently written.

<br/>You read history when you want to see what has changed, when searching a bug, what the difference is between branches, and so on.

<br/>The argument of "I want the history to look like exactly how it really happened" is flawed, because very often your history is suboptimal (you commit a feature, and shortly afterwards you commit a fix for that feature, or a commit that contains separate logical changes/bugfixes)

<br/>This makes history more complicated to read then it should be, so for all the folks who will ever look back at your history (even if you think that will only be yourself) a clean history is more easy to "get", just like clean source code.

<br/>Also, part of the awesomeness of git is that juggling with features (needed for debugging, trying things out, ..) in your code is so flexible (see the git commit/branch model), but if you have logical changes spread over multiple commits, or one commit containing multiple logical changes, this gets painful very quickly.

<br/>Once you figure out history rewriting (and it's pretty easy to learn, really!) it only costs a little time to clean up your history, which will pay off in a much greater extent for every time you or somebody else wants to look at, or needs to work <i>with</i> it. (again, just like source code itself!)

<br/>This also means that you don't need to spend so much time thinking about your commit messages for commits that are merely fixups or small additions to other logical changes.  Because those will be squashed into the other commits anyway.

I usually commit frequently, but end up squashing many commits together, my commit log easily gets compressed by a factor two or more.  The less history, the better. (just like source code!)

<br/>The commits you actually push (especially when pushing to a master branch) should of course be clean, accuractly described and with correct author information, for obvious reasons such as readability.

</p>

<p>

Note that there is some kind of <i>paradox</i>: you can only achieve "perfect history" if your commits are well-tested and every introduced feature has no bugs (has all bugfix commits squashed into it), but at the same time, you can only properly expose new code by making it public, and it only gets widely used and tested if it's in your main (master) branch.

<br/>This is one of the reasons why a workflow model such as one based on topic branches (aka feature branches) works: you see, git by default doesn't allow non-fast-forward pushes.

Because you obviously don't want to break the history of other people following your stable (master branch) development.  So once you push to master, it should usually be there for good.

<br/>As far as I can see, it is accepted in most projects (those run by folks with git expertise?) to push non-fast-forward to topic branches.  The idea being a topic branch is a "work in progress" branch, it is made public so multiple people can review/work on it.  Based on that work/review, its history will often get rewritten through a non-fast-forward push.  And if you're following/working on such a branch, you should be clever enough to deal with changed history.

<br/>So, a topic branch allows you to make changes public, get feedback, clean up the history of the patchset you (and maybe others) are working on, and when satisfied, you can push to master.

<br/>There is still a chance you'll later need to push bugfixes to master, but this will happen much more infrequently, so while there is no perfect workflow model that creates perfect history (in master) combined with perfect usability (no need to handle non-fastforward pushes) I find this model brings a quite good compromise.

</p>



<p>

To paraphrase, I would say:

<br/><i>You should care about clean vcs history for the same reasons you should care about clean code</i>.

<br/>Just like using git is good to progressively help reaching better software, so is git history rewriting good for progressively reaching a better git history.  Version control on top of version control, if you will.  A very crude form of version control but I don't think it needs to be any more advanced then this.

</p>



<h3>Why should I write my commits in imperative present tense ('do foo') rather then past tense ('did foo')?</h3>

<p>

Git developers command doing this (at least for the <a href="http://repo.or.cz/w/git.git">git project</a>), but they did not document <em>why</em>'s.

Some commonly cited reasons:

<ul>

<li>Consistency.  That's how it is in many projects (including git itself). Also git tools that generate commits (like git merge or git revert) do it.</li>

<li>It's usually shorter</li>

<li>You can name commits more consistently with titles of tickets in your issue/feature tracker (which don't use past tense, although sometimes future)</li>

</ul>

Another reason I came up with: people not only read history to know "what happened to this codebase",

but also to answer questions like "what happens when I cherry-pick this commit", or "what kind of new things will happen to my code base because of these commits I may or may not merge in the future".

(Note that these are questions about the past,current and future)

This is more a subjective topic, but I feel that the best way to capture this time-independence of a commit is to write down as time-agnostic as possible,

and something like 'do foo' (which could be 'do foo in the future', for instance) is more generic then something with a sense of time hardwired in it ("did foo" or "will do foo")

</p>

<p>

See also

<ul>

<li><a href="http://git.kernel.org/?p=git/git.git;a=blob;f=Documentation/SubmittingPatches;h=ece3c77482b3ff006b973f1ed90b708e26556862;hb=HEAD">Git contributor guidelines</a></li>

<li><a href="http://progit.org/book/ch5-2.html">ProGit: contributing to a project</a></li>

<li><a href="http://en.wikibooks.org/wiki/Git/Introduction#Good_commit_messages">WikiBooks Git introduction</a></li>

</ul>

</p>
