+++
title = "PhpDeliciousClient"
date = "2007-06-29T13:52:21-04:00"
tags = ["web2.0", "php", "foss", "bash"]
+++
<p>PhpDeliciousClient is a CLI program for administering your Delicous account.  When you invoke it from the command line you have some methods to administer your tags and your posts.</p>

<p>It's written in PHP and uses <a href="http://www.ejeliot.com/">Ed Eliot's</a> <a href="http://www.ejeliot.com/pages/php-delicious">PhpDelicous</a> class to contact the del.icio.us api. (included in download)<br />

PhpDeliciousClient is licensed under the GPL v2, while the PhpDelicious class is licensed under the BSD license.</p>

<h3>Why?</h3>

<p>The main reason I started developing it is because administering your account on the del.ico.us web interface can be cumbersome.<br />

This is especially true in the case of balancing your tags:<br />

After a while, your del.icio.us account can get unbalanced: this is when you have many tags, but most of them only contain a few posts (very often even just one! ).<br />

So you would want to balance them again, by deleting and renaming some very specific tags so that you get a collection consisting of less tags (who are more general) and contain about 10 ~ 30 posts each.  Maybe you even also want to delete or rename some general ones who have way to many associated posts.<br />

If you want to do this via the del.icio.us web interface you could either go to your personal page, click a tag, and delete the tag manually from each associated post.  Or you could go to the delete or rename tag pages.  On these pages you have a form where you can select an existing tag from a dropdown (which usually is huge) and choose to delete or rename it (depending on which page you are on).  Then you would need to go to the form again and do this again for each tag.</p>

<p>With this tool, you can get a list of tags with certain conditions.  Eg "show me all tags who have between 1 and 3 associated posts".  You can then loop through that list and for each tag the tool will present you the option to delete, rename or skip it.</p>

<p>Of course it can do more, but this was my focus: making balancing an account as pleasant as possible.  Other features, such as adding or editing single posts are considered less important as these things can be done just fine on the del.icio.us page.</p>

<h3>Current state</h3>

<p>Currently the tool seems to do what it is intended to (and pretty well, at least for me: I cleaned up my account from about 400 to 80 tags during development of this program).<br />

However I don't give any warranty, the tool is only moderately documented, performs little to no user input checking and isn't very well tested so don't expect any higher quality then that of the average Microsoft product.<br />

This program shouldn't empty your del.icio.us account or blow up your computer but if it does I cannot be held responsible.</p>

<h3>Supported features</h3>

<ul>

<li>[t] View Tag: Based on the name of tag you enter, you can see the associated posts and edit or rename the tag.</li>

<li>[ts]  View Tags: Shows you all tags based on certain criteria:

<ul>

<li>lowerlimit: the minimum amount of times a tag has to be associated to a post</li>

<li>upperlimit: the maximum amount of times a tag has to be associated to a post</li>

<li>hard limit: the maximum number of tags you wish to edit/view at once</li>

</ul>

<p>You can decide to view associated posts for each tag, and you can choose wether to only show the tags, or to present you a menu with options for each one.  I usually use the latter, along with associated posts viewing enabled.</li>

<li>[p] View Post: shows you the first hit based on a tag and url*</li>

<li>[ps] View Posts: shows you all posts based on a tag and url*</li>

<li>[lu] Date of last update: Shows you the time when the data (on the serverside) last changed</li>

</ul>

<p>*: url based searching is still buggy, I'm working on it.</p>

<h3>Plans for the future</h3>

<p>My goals for upcoming releases are (aside from bug fixing) to add features to let you do stuff that you currently can't do or at least not in a productive manner.  </p>

<h4>Known bugs to be fixed</h4>

<ul>

<li>URL-based post querying doesn't work</li>

<li>Timezone not taken into account or something like that, because the "last updated" date has a 2hrs offset for me</li>

<li>During list iteration tags that have been renamed/deleted already still appear in posts for other tags</li>

<li>Issue less load on the Del.icio.us webservice by using the updated date (gonna take a look at Ed's caching system for that)</li>

</ul>

<h4>Features I have on my mind</h4>

<ul>

<li>Try to hide password as it is typed in by user</li>

<li>When a tag has many associated posts, automatically show them more concisely</li>

<li>An "are you sure?" thing when you want to rename to a tag that already has many (say: 40) associated posts</li>

<li>A mode to only show tags that differ one letter, or differ several letters, as long as they have enough in common (say: 2/3, 1/2 or user configurable)</li>

<li>An improved commandline that allows commands/queries like "rm tag1 tag2 tag3"

</ul>

<h3>Prerequisites</h3>

<ul>

<li>A shell (such as bash)</li>

<li>PHP 4 or higher, with php-cli enabled (default)</li>

<li>A del.icio.us account, preferrably a very messy one</li>

</ul>

<h3>Download</h3>

<p><a href="http://users.edpnet.be/dieter/php_delicious_client_v05.zip" onClick="javascript:urchinTracker ('/files/php_delicious_client_v05.zip');">release v0.5 (1-7-2007)</a></p>

<h3>Installation</h3>

<p>Unpack the archive and put the directory somewhere on your system.  On Linux /usr/local/bin/ is usually a good choice.<br />

Make sure pdclient.php has the executable flag (x).  If the directory is in your $PATH, you can just type pdclient.php on your console, otherwise you need to type &lt;path to program&gt;/phpdeliciousclient/pdclient.php or edit your $PATH.</p>

<p>You could also create a symlink in a good directory: <em>ln -s &lt;path to program&gt;/phpdeliciousclient/pdclient.php /usr/local/bin/pdclient</em></p>

<h3>Usage</h3>

<p>I choose a mysql-like syntax for invoking the program.  Valid options are:</p>

<ol>

<li><em>pdclient.php</em></li>

<li><em>pdclient.php --help</em></li>

<li><em>pdclient.php --user &lt;delicious username&gt;</em></li>

<li><em>pdclient.php --user &lt;delicious username&gt; --password</em></li>

<li><em>pdclient.php --user &lt;delicious username&gt; --password &lt;delicious password&gt;</em></li>

</ol>

<p>With method #4, the program will ask your password upon execution.  With the other methods this doesn't happen.  You can always update your account information from the menu. (<em>account setup</em>)</p>

<p>In the program prompt you can always type 'h' to get help.  Aside from that, just try the options, you'll figure it out in no time.</p>

<h3>Bug reports &amp; feature requests</h3>

<p>You can report bugs or file feature requests through the comment system on this page. Choose an appropriate title and prefix it with "Bug: " or "Feature: "</p>
