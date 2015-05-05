+++
title = "Upgrading Drupal the easy way"
date = "2007-07-29T15:57:23-04:00"
tags = ["drupal"]
+++
<p>Here is a synthesized version of the upgrade instructions that came with the package:</p>

<ol>

<li>Backup your database and Drupal directory.  Especially your site settings, custom modules and themes, and files folder.</li>

<li>Log on as the user with user ID 1.  User ID 1 needs to be logged in so that you can access update.php (step 9) which can only be run by user ID 1.  Do not close your browser until step 10 is complete.</li>

<li>Place the site in "Off-line" mode, to mask any errors from site visitors.</li>

<li>Disable contributed modules and switch to a core theme</li>

<li>Remove all of the old files and directories from the Drupal installation directory.</li>

<li>Unpack the new Drupal files and directories into the Drupal installation directory.</li>

<li>Copy the backed up files/directories from step 1 to the Drupal installation directory.</li>

<li>Verify the new configuration file to make sure it has the latest and correct information.</li>

<li>Re-install contributed modules.   Check if they are compatible with the new version</li>

<li>Run update.php by visiting <a href="http://www.example.com/update.php" title="http://www.example.com/update.php">http://www.example.com/update.php</a></li>

<li>Finally, return site to "Online" mode</li>

</ol>

<p>Now, the thing is you don't have to do things like disabling contributed modules and themes if you install them right away instead of later on.</p>

<p>So, here are my simplified instructions:</p>

<ol>

<li>Unpack the drupal 5.2 folder on your local system</li>

<li>Copy all your specific folders/files (files, themes, modules and settings.ini) to the right place in this folder</li>

<li>Login as user 1</li>

<li>Enable offline mode</li>

<li>Delete all files of your Drupal installation on the webhost</li>

<li>Upload the files from the drupal 5.2 folder to your webhost</li>

<li>go to <a href="http://www.example.com/?q=user" title="http://www.example.com/?q=user">http://www.example.com/?q=user</a> and login again</li>

<li>Run <a href="http://www.example.com/update.php" title="http://www.example.com/update.php">http://www.example.com/update.php</a></li>

<li>Enable online mode</li>

</ol>

<p>These instructions worked fine for upgrading from 5.1 to 5.2.  If you do are more drastic upgrade (e.g. from 4 to 5) you should only follow this method if you don't have any contributed themes/modules because otherwise you need to upgrade your modules.</p>
