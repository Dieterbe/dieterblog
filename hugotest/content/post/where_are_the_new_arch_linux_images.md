+++
title = "Where are the new Arch Linux release images?"
date = "2011-05-17T21:29:58-04:00"
tags = ["linux", "foss", "arch"]
+++
<p>This is a question I get asked a lot recently.  The latest <a href="http://www.archlinux.org/download/">official images</a> are a year old.  This is not inherently bad, unless you pick the wrong mirror from the outdated mirrorlist during a netinstall, or are using hardware which is not supported by the year old kernel/drivers.  A core install will yield a system that needs drastic updating, which is a bit cumbersome.  There are probably some other problems I'm not aware of.  Many of these problems can be worked around (with 'pacman -Sy mirrorlist' on the install cd for example), but it's not exactly convenient.</p>



<p>Over the past years (the spare time in between <a href="/my_metalband.html">the band</a>, my search for an apartment in <a href="http://en.wikipedia.org/wiki/Ghent">Ghent</a> and a bunch of other things) I've worked towards fully refactoring and overthrowing how releases are being done.  Most of that is visible in the <a href="http://projects.archlinux.org/users/dieter/releng.git/">releng build environment repository</a>.

Every 3 days, the following happens automatically:

<ul>

<li>packages to build images (archiso) and some of which are included <i>on</i> the images (aif and libui-sh) get rebuilt.  They are actually git versions, the latter two have a separate develop branch which is used. Normal packages get updated the normal way.</li>

<li>the images are rebuilt, and the dual images get generated</li>

<li>the images, the packages and their sources are synced to the public on <a href="http://releng.archlinux.org/">http://releng.archlinux.org</a></li>

</ul>

Actually things are <a href="http://projects.archlinux.org/users/dieter/releng.git/tree/scripts/releng-build-and-release-testing.sh">bit more involved</a> but this is the gist of it.  All of this is now run on a <a href="https://wiki.archlinux.org/index.php/Category:DeveloperWiki:Server_Configuration#Releng_server_.28alberich.29">dedicated VPS</a> donated by <a href="http://www.airvm.com/">airVM</a>.</p>



<p>I never really completed the <a href="/aif_automatic_lvm_dm_crypt_installations_and_test_suite.html">aif automatic test suite</a>, somewhere along the way I decided to focus on crowdsourcing test results.

The weight of testing images (and all possible combinations of features) has always been huge, and trying to script tasks would either get way complicated or insufficient.

So the new approach is largely inspired by the core and testing repositories:  we automatically build testing images, people report feedback, and if there is sufficient feedback for a certain set of images (or a bunch of similar sets of images) that allows us to conclude we have some good material, we can promote the set to official media.

<br/>The latest piece of the puzzle is the new <a href="http://www.archlinux.org/releng/feedback/">releng feedback application</a> which <a href="http://zasshi-slash.blogspot.com/">Tom Willemsen</a> contributed. (again: outsourcing FTW).  It is still fairly basic, but should already be useful enough.  It lists pretty much all features you can use with archiso/AIF based images and automatically updates the list of isos based on what it sees appearing online, so I think it will be a good indicator on what works and what doesn't, and that for each known set of isos.</p>

<p>So there. <b>Bleeding edge images for everyone</b>, and for those who want some quality assurance: <b>the more you contribute, the more likely you'll see official releases</b>.



<p>While contributing feedback is now certainly very easy, don't think that only providing feedback is sufficient, it takes time to maintain and improve aif and archiso as well and contributions in that department are still very welcome.

I don't think we'll get to the <a href="http://www.archlinux.org/news/200902-iso-release/">original plan</a> of official archiso releases for each stable kernel version, that seems like a lot of work despite all the above.</p>



<p>As for what is new: again too much to list, here is a <a href="http://releng.archlinux.org/isos/Changelog">changelog</a> but I stopped updating it at some point.  I guess the most visible interesting stuff is friendlier package dialogs (with package descriptions), support for nilfs, btrfs and syslinux (thanks <a href="http://pyther.net/">Matthew Gyurgyik</a>), and an issues reporting tool.

Under the hood we refactored quite a bit, mostly blockdevice related stuff, config generation and the "execution plan" (like, how each function calls each other and how failures are tracked) in AIF has been simplified considerably.</p>



<!-- I used to be pedantic about details like "all packages installed in the live environment must be available in the official core/extra repositories but i might become a bit less strict.  or maybe not, it's not hard to switch to official packages. -->
