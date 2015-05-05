+++
title = "Handling a remote rename/move with Git"
date = "2008-11-17T11:29:36-04:00"
tags = ["foss", "git"]
+++
<p>You can do this in two ways:</p>

<ul>

<li>open .git/config and modify the url for the remote manually</li>

<li>git remote rm origin &amp;&amp; git remote add origin git@github.com:$user/$project.git</li>

</ul>

<p>That's it! All will work fine again.</p>
