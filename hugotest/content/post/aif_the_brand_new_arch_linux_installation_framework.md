+++
title = "AIF: the brand new Arch Linux Installation Framework"
date = "2008-11-17T11:45:25-04:00"
tags = ["linux", "foss", "arch"]
+++
<p>Recently I started thinking about writing my own automatic installer that would set up my system exactly the way I want.<br />

(See <a href="/rethinking_the_backup_paradigm_a_higher-level_approach" title="/rethinking_the_backup_paradigm_a_higher-level_approach">rethinking_the_backup_paradigm_a_higher-level...</a>)</p>

<p>I looked at the official Arch install scripts to see if I could reuse parts of their code, but unfortunately the code was just one big chunk of bash code with the main program and "flow control" (you must first do this step, then that), UI-code (dialogs etc) and backend logic (create filesystems, ...) all mangled up and mixed very closely together.<br />

Functionality-wise the installer works fine, but I guess the code behind it is the result of years of adding features and quick fixes without refactoring, making it impossible to reuse any of the code.</p>

<p>So I started to write <a href="http://github.com/Dieterbe/aif/">AIF: the Arch Linux Installation Framework</a><!--more--> (actually it had another name until recently), with these 3 goals in mind:</p>

<ul>

<li>Make all code modular, reusable etc.  Everyone should be able to add/change/remove change certain aspects of an installation procedure easily or build custom installation relying on existing code where appropriate</li>

<li>Port /arch/setup and /arch/quickinst, so you get (almost) the same installer as before, but using totally refactored code.</li>

<li>Write my own automatic procedure for my own custom needs</li>

</ul>

<p>Right now most of the hard work is done and the ported version of /arch/setup seems to work more or less.<br />

I've posted to the arch-general mailing list and the responses I got were very positive.<br />

This is what Aaron Griffin (lead developer of Arch Linux) said:</p>

<blockquote><p>

My honest opinion is that this is awesome. You're the reason I love open source 8)</p>

<p>That said, we haven't release a 2.6.27 ISO just yet, and I need to go<br />

in panic mode and get it out this weekend. But for the next release,<br />

or even a smaller release before then, I'd *love* to incorporate this.</p>

<p>(...)</p>

<p>Just letting you know: I'm not silent because I don't care. I'm silent<br />

because I'm watching and drooling 8)

</p></blockquote>

<p>You can read the whole thread here: <a href="http://www.nabble.com/Fifa:-Flexible-Installer-Framework-for-Arch-linux-td20256427.html" title="http://www.nabble.com/Fifa:-Flexible-Installer-Framework-for-Arch-linux-td20256427.html">http://www.nabble.com/Fifa:-Flexible-Installer-Framework-for-Arch-linux-...</a></p>

<p>I've also built <a href="http://aur.archlinux.org/packages.php?SeB=m&amp;K=Dieter_be">packages</a> to make it easy to install on a current installcd.  The package also comes with a <a href="http://github.com/Dieterbe/aif/tree/master/README">readme</a> and <a href="http://github.com/Dieterbe/aif/tree/master/HOWTO">howto</a> that explain how to install and use AIF.</p>

<p>Right now I encourage people to try it out.  All known bugs are documented in the TODO file, there are probably more that I didn't discover yet.  But it should work pretty well.<br />

I'm very curious for input on the code/design level as well.</p>

<p>Hopefully the Arch guys can set me up with a bugtracker and make some sort of announcement to the community to try it out...</p>
