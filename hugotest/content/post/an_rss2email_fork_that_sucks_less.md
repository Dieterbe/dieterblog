+++
title = "An rss2email fork that sucks less"
date = "2010-09-25T20:33:08-04:00"
tags = ["python", "foss"]
+++
<p><a href="http://www.allthingsrss.com/rss2email/">Rss2email</a> is a great tool.  I like getting all my news messages in my mailbox and using smtp to make the "news delivery" process more robust makes sense.<br />

However, there are some things I didn't like about it so I made a <a href="http://github.com/Dieterbe/rss2email/">github repo</a> where I maintain an alternative version which (imho) contains several useful improvements, both for end users and for developers/downstreams.<br />

Also, this was a nice opportunity for me to improve my python skills :)</p>

<p>Here is how it compares:<br />

<!--more--><br />

(most of the changes are only in the xdg branch, which is the one I use and test)</p>

<table>

<tr>

<th>criterion</th>

<th>official version</th>

<th>my fork</th>

</tr>

<tr>

<td>code hosting/release process</td>

<td>"release" = tarball containing updated code corresponding to various fixes, and snapshots of other projects (dependencies).  no version control, not even separate patches.  no bug tracker.</td>

<td>git. upstream tracking branch, master branch (basic "good stuff" patches), XDG topic branch (my favorite).  Does not include code from other projects, rather list dependencies.  Github issue tracker</td>

</tr>

<tr>

<td>code style</td>

<td>dirty (extraneous whitespace, ^M characters, incorrect permissions, loads of bogus [whitespace] changes, ..).  The python code itself seems nice though</td>

<td>clean</td>

</tr>

<tr>

<td>file storage &amp; config</td>

<td>all in ~/.rss2email, list of feeds, email address and feeds state go into pickle file. commands like 'r2e add', 'r2e delete', 'r2e list' to manage feeds. feed ids change when feeds get deleted.  'r2e email' to manage email adress.</td>

<td>adherence to xdg basedir spec. list of feeds goes into plaintext file, so does email address.  state in separate pickle file.  removed all the [now pointless] commands.</td>

</tr>

<tr>

<td>Temporary disabling of feeds</td>

<td>no (if you remove a feed, you loose the state info)</td>

<td>yes.  comment it out or remove it.  state info won't be lost</td>

</tr>

<tr>

<td>installation/runtime</td>

<td>no Makefile.  no reliance on $PATH, locking code in python.  Distros are applying patches and/or using custom wrapper scripts</td>

<td>smarter wrapperscript that prevents multiple runs, so removed locking code from python.  Has Makefile.  Easy to package</td>

</tr>

<tr>

<td>logging/debugging</td>

<td>useful info messages hidden by default, "verbose mode" and error messages using print calls all over the place</td>

<td>useful messages on stdout.  additional (info/warn/error/..) logging and debuglogging use python module (xdg compliant)</td>

</tr>

<tr>

<td>web ui</td>

<td>yes</td>

<td>no (I don't need it)</td>

</tr>

<tr>

<td>windows support</td>

<td>yes</td>

<td>no (unless somebody ports xdg to windows and updates the wrapper script)</td>

</tr>

</table>

<p>Other then that, there are also some smaller fixes in various places.</p>

<p>I'm using my version "in production" and it works great for me so far.<br />

I have contacted the author and told her about my changes, but no response yet.<br />

For now, you can treat this as an alternative version that stands on it's own.  I made an Arch <a href="http://aur.archlinux.org/packages.php?ID=41136">rss2email-xdg-git</a> package in the AUR.</p>

<p>Oh, and I'm liking python :)  Pretty nice and powerful language.</p>
