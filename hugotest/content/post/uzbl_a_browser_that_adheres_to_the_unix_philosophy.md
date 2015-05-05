+++
title = "Uzbl.  A browser that adheres to the unix philosophy."
date = "2009-04-27T23:02:37-04:00"
tags = ["uzbl", "foss"]
+++
<p>I need a browser that is fast, not bloated, stores my data (bookmarks, history, account settings, preferences, ...) in simple text files that I can keep under version control, something that does not reinvent the wheel, something that I can control.</p>

<p>Well, I could not find it.<br />

So I started the <a href="http://bbs.archlinux.org/viewtopic.php?id=70700&amp;p=1">uzbl browser</a> project.<!--more--><br />

The project is just a few days old, but already some developers joined me and we're having a lot of fun hacking.  One of them (Mike) was even creazy enough to register a domain for it with a website and all.<br />

So there you have it: <a href="http://uzbl.org">uzbl.org</a>.<br />

It is stil very early in the process, but some things already work.</p>

<p>Here are some of the ideals (not all implemented yet):</p>

<ul>

<li>keyboard controlled: modal with vim-like bindings, or with modifier keys</li>

<li>very simple ini-style config file</li>

<li>very minimal interface. No unnecessary interface elements</li>

<li>Things like url changing, loading/saving of bookmarks, ... are handled through external scripts that you write and call with keyboard shortcuts.  If they want to alter the behavior of uzbl (change url, reload,..) they write a command to a FIFO (spawned by the uzbl process).  Some scripts are also triggered by uzbl (like history logging or when a file needs to be downloaded) </li>

</ul>

<p><a href="http://github.com/Dieterbe/uzbl/tree/master">more</a></p>

<p>Uzbl follows the UNIX philosophy:<br />

<quote><br />

<i>Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.</i></quote></p>
