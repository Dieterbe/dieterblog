+++
title = "Restoring accidental git force push overwrite on GitHub if you don't have the needed commits locally"
date = "2016-11-14T11:33:03+02:00"
tags = ["git"]
+++

I [like cleaning git history](http://dieter.plaetinck.be/post/why-rewriting-git-history-and-why-commits-imperative-present-tense/), in feature branches, at least.
The goal is a set of logical commits without other cruft, that can be cleanly merged into master.  This can be easily achieved with git rebase and force pushing to the feature branch on GitHub.

Today I had a little accident and found myself in this situation:

* I accidentally ran `git push origin -f` instead of my usual `git push origin -f branchname` or `git push origin -f HEAD`
* This meant that I not only overwrote the branch I wanted to update, but also by accident a feature branch (called `httpRefactor` in this case) to which a colleague had been force pushing various improvements which I did not have on my computer.  And my colleague is on the other side of the world so I didn't want to wait until he wakes up. (if you can talk to someone who has the commits just have him/her re-force-push, that's quite a bit easier than this)
  It looked something like so:

```
$ git push origin -f
  <here was the force push that succeeded as desired>
+ 92a817d...065bf68 httpRefactor -> httpRefactor (forced update)
```

**Oops!**
So I wanted to reset the branch on GitHub to what it should be, and also it would be nice to update the local copy on my computer while we're at it.
Note that the commit (or rather the abbreviated hash) on the left refers to the commit that was the latest version in GitHub, i.e. the one I did not have on my computer.
A little strange if you're to accustomed to `git diff` and `git log` output showing hashes you have in your local repository.

Normally in a git repository, the objects dangle around until `git gc` is run, which clears any commits except those reachable by any branches or tags.
I figured the commit is probably still in the GitHub repo (either cause it's dangling, or perhaps there's a reference to it that's not public such as a remote branch), I just need a way to attach a regular branch to it (either on GitHub, or fetch it somehow to my computer, attach the branch there and re-force-push), so step one is finding it on GitHub.

The first obstacle is that GitHub wouldn't recognize this abbreviated hash anymore: going to 
`https://github.com/raintank/metrictank/commit/92a817d` resulted in a 404 commit not found. 

Now, we use CircleCI, so I could see what had been the full commit hash in the CI build log.
Once I had it, I could see that `https://github.com/raintank/metrictank/commit/92a817d2ba0b38d3f18b19457f5fe0a706c77370` showed it.
An alternative way of opening a view of the dangling commit we need, is using the reflog syntax.
[Git reflog](https://git-scm.com/docs/git-reflog) is a pretty sweet tool that often comes in handy when you made a bit too much of a mess on your local repository,
but also on GitHub it works:  if you navigate to `https://github.com/raintank/metrictank/tree/httpRefactor@{1}` you will be presented with the commit
that the branch head was at before the last change, i.e. the missing commit, 92a817d in my case.


Then follows the problem of re-attaching a branch to it.
Running on my laptop `git fetch --all` doesn't seem to fetch dangling objects, so I couldn't bring the object in.

Then I tried to create a tag for the non-existant object.  I figured, the tag may not reference an object in my repo, but it will on GitHub, so if only I can create the tag, manually if needed (it seems to be just a file containing a commit hash), and push it, I should be good.
So:
```
~/g/s/g/r/metrictank ❯❯❯ git tag recover 92a817d2ba0b38d3f18b19457f5fe0a706c77370
fatal: cannot update ref 'refs/tags/recover': trying to write ref 'refs/tags/recover' with nonexistent object 92a817d2ba0b38d3f18b19457f5fe0a706c77370
~/g/s/g/r/metrictank ❯❯❯ echo 92a817d2ba0b38d3f18b19457f5fe0a706c77370 > .git/refs/tags/recover
~/g/s/g/r/metrictank ❯❯❯ git push origin --tags
error: refs/tags/recover does not point to a valid object!
Everything up-to-date
```

So this approach won't work.  I can create the tag, but not push it, even though the object exists on the remote.

So I was looking for a way to attach a tag or branch to the commit on GitHub, and then I found a way.
While having the view of the needed commit open, click the branch dropdown, which you typically use to switch the view to another branch or tag.
If you type any word in there that does not match any existing branch, it will let you create a branch with that name. So I created `recover`.

From then on, it's easy.. on my computer I went into `httpRefactor`, backed my version up as httpRefactor-old (so I could diff against my colleague's recent work), deleted httpRefactor, and set it to
the same commit as what origin/recover is pointing to, pushed it out again, and removed the recover branch on GitHub:

```
~/g/s/g/r/metrictank ❯❯❯ git fetch --all
(...)
~/g/s/g/r/metrictank ❯❯❯ git checkout httpRefactor
~/g/s/g/r/metrictank ❯❯❯ git checkout -b httpRefactor-old
Switched to a new branch 'httpRefactor-old'
~/g/s/g/r/metrictank ❯❯❯ git branch -D httpRefactor
Deleted branch httpRefactor (was 065bf68).
~/g/s/g/r/metrictank ❯❯❯ git checkout recover
HEAD is now at 92a817d... include response text in error message
~/g/s/g/r/metrictank ❯❯❯ git checkout -b httpRefactor
Switched to a new branch 'httpRefactor'
~/g/s/g/r/metrictank ❯❯❯ git push -f origin httpRefactor
Total 0 (delta 0), reused 0 (delta 0)
To github.com:raintank/metrictank.git
 + 065bf68...92a817d httpRefactor -> httpRefactor (forced update)
~/g/s/g/r/metrictank ❯❯❯ git push origin :recover                                                                                                                                            ⏎
To github.com:raintank/metrictank.git
 - [deleted]         recover
```

And that was that... If you're ever in this situation and you don't have anyone who can do the force push again, this should help you out.
