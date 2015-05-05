+++
title = "facebook usrbincrash php implementation"
date = "2010-02-12T23:25:46-04:00"
tags = ["php", "perf"]
+++
<p>I haven't touched the code for a few months, but better to put it online then to let it rot.<br />

<a href="http://github.com/Dieterbe/facebookpuzzles/" title="http://github.com/Dieterbe/facebookpuzzles/">http://github.com/Dieterbe/facebookpuzzles/</a></p>

<p>2 branches:</p>

<ul>

<li>master: basically what I submitted to FB, and what just works</li>

<li>withpruning: an attempt for futher optimalisation (it only improves the runtime in some cases) but I didn't finish that version and there's a bug in it somewhere</li>

</ul>

<p>In the repo you'll also find various test input files supplied by the community on <a href="http://www.facebook.com/topic.php?uid=15325934266&amp;topic=5131&amp;post=30091">the forums</a> and a script to benchmark the implementation on all inputfiles.</p>
