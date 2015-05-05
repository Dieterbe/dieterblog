+++
title = "Checking if a git clone has any unique content, git/svn scripts"
date = "2010-12-16T18:06:23-04:00"
tags = ["git"]
+++
I heard bzr (or was it hg...) can do it out-of-the-box, but I couldn't find any existing solution for git.<br />

So I wrote a script to do this.  It checks a repo for unique commits, tags, branches, dirty files/index, added files, or stashed states.  In comparison to a specific remote, or all of them, and uses an appropriate exitcode.<br />

<a href="https://github.com/Dieterbe/git-scripts/blob/master/git-remote-in-sync.sh">git-remote-in-sync.sh</a><br />

The script is part of a bigger <a href="https://github.com/Dieterbe/git-scripts/">git-scripts</a> repo (most of the scripts written by random people).  Although the original repo creator hasn't gotten back to me this seems like a good starting point to have some sense of order in the wildspread of git scripts.</p>

<p>Here are some other scripts I find pretty useful:<!--more--></p>

<ul>

<li><a href="https://github.com/Dieterbe/git-scripts/blob/master/git-ignore-wizard">git-ignore-wizard</a>: dmenu-file-selector for adding ignore rules because I always forget which file to use for which use-case.</li>

<li><a href="https://github.com/Dieterbe/git-scripts/blob/master/git-root">git-root</a>: get the path of the git root</li>

<li><a href="https://github.com/Dieterbe/git-scripts/blob/master/git-merge-repo">git-merge-repo</a>: haven't tried this, but looks neat</li>

</ul>

<p>On the topic of scripts for VCS'es, I also have one for svn.<br />

This one is for those occasions where you have a directory tree in svn, and you want to replace the entire tree by another tree.  The structure can be completely different (files, directories added/renamed,removed, etc) and it becomes painful to do it manually, if you even manage to keep svn from going berzerk on you.<br />

<a href="https://github.com/Dieterbe/svn-scripts/blob/master/svn-replace-subtree">svn-replace-subtree</a> takes care of it.</p>
