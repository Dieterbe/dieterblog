+++
title = "DDM : a Distributed Data Manager"
date = "2008-03-29T20:28:16-04:00"
tags = ["life", "foss", "bash"]
+++
<p><b>UPDATE: this information is outdated.  See <a href="http://github.com/Dieterbe/ddm/tree/master" title="http://github.com/Dieterbe/ddm/tree/master">http://github.com/Dieterbe/ddm/tree/master</a> for latest information.</b></p>

<h3>Introduction</h3>

<p>If you have multiple sets of data (e.g.: music, images, documents, movies, ...) and you use these on more then one system ( e.g. a laptop and a file server) then you probably also have some 'rules' on how you use these on your systems.  For example after capturing new images you maybe put them on your laptop first but you like to sync them to your file server frequently.  On the other hand you also want all your high-res images (stored on the server) available for editing on the laptop, and to make it more complicated you might have the same images in a smaller format on your server (for gallery programs etc.) and want these (or a select few albums of them) available on the road. </p>

<p>The more different types of data you have and the more you have specific work flows the harder it becomes to keep your data as up to date as possible and consistent on your boxes.  You could manually rsync/(s)cp your data but you end up in having a mess (at least that's how it turned out on my boxes). Putting everything under version control is great for text files and such, but it's not an option for bigger (binary) files.</p>

<p>I wanted to keep all my stuff neatly organised in my home directories and I want to create good work flows with as minimum hassle as possible, so I decided to write DDM: the Distributed Data Manager.<!--more--></p>

<h3>Disclaimer</h3>

<p>The code is far from finished.  Some features are still missing and there will be bugs in it.  I'm even still thinking about the concepts themselves.   Don't blame me if ddm deletes the wrong files or causes your computer to blow up.</p>

<h3>Concepts</h3>

<p>DDM is a bash script that manages your data, distributed over multiple (*nix) systems.  You tell it how you want to work with your data and ddm will do the copying, deleting, syncing, committing, updating, ... for you.<br />

It uses simple things like cp, rsync and svn for this.<br />

Configuration is done through simple text files that will be sourced.</p>

<p>Ddm works with repositories: these are data stores on your server which should never be edited by hand.  A repository can be a svn repository or something as simple as a directory shared over the network ( through NFS, SMB, ... )</p>

<p>I highly recommend <a href="http://wiki.autofs.net/">autoFS</a> as auto mounter.  It is very easy, yet powerful and flexible.</p>

<h4>Vocabulary</h4>

<ul>

<li>repotype: the type of your repo.  currently this is either 'svn' (subversion) or 'vfs' ( any position in your VFS, the underlying technology is up to you. although autofs+nfs will be most useful)</li>

<li>dataset name: The name of your dataset. e.g. 'movies'</li>

<li>dataset type (see below)</li>

<li>action: commit, update, checkout</li>

</ul>

<h4>Dataset types</h4>

<ul>

<li>selection: a copy of a subset of the data in the repo (e.g. your favourite movies of all your movies)</li>

<li>buffer: temporary storage to be flushed to the repo regularly (e.g. new images or stuff you just downloaded)</li>

<li>copy: (default): a copy of all content in the repo (an svn working copy or a directory using rsync)</li>

<li>extension: contains unique content that you don't want on your server (e.g. temporary files)</li>

<li>direct: a (symlink to a) local mount point for a remote location. useful for big collections</li>

</ul>

<p>So basically you tell ddm to perform an action on a dataset of a specific type.<br />

Note that some actions wouldn't make sense for some dataset types ( e.g. commit on a selection or extension) and thus don't need to be implemented, while others perform really basic operations (an update of a vfs copy is just an rsync) or just wrap around something else (notably the svn actions just wrap around the svn tool)<br />

Keep in mind though that everything can be overridden through .ddm files in dataset directories.</p>

<h4>Configuration</h4>

<p>Ddm is configured through:</p>

<ul>

<li>a .ddm file in your home directory. (needed)</li>

<li>a .ddm file in your dataset directories (optional)</li>

<li>the directory name of your dataset (read on) (optional)</li>

</ul>

<p>To specify the dataset type, the easiest way is to add suffixes to your directories. eg video-selection.  This is not a must and can be specified in the .ddm file in the dataset directory. For the 'copy' dataset type you don't need to specify anything (it's default)<br />

Unless overridden, ddm will construct the repo path as follows:  </p>

{{< highlight "bash" "style=default" >}}<![CDATA[

$TYPE_BASE/$TYPE_PREFIX$DATASET_NAME$TYPE_SUFFIX

]]>{{< /highlight >}}<p>(if unclear, read on)</p>

<p>In the .ddm file in your dataset directory you can override defaults.</p>

<h5>~/.ddm</h5>

<p>This is how my file looks like.</p>

{{< highlight "bash" "style=default" >}}<![CDATA[

ALLOWED_REPO_TYPES='svn vfs'

DEFAULT_REPO_TYPE='vfs'



SVN_BASE='https://server/svn/repos/'

SVN_PREFIX='ddm-'

VFS_BASE='/net/server/home/dieter/ddm-repo'

]]>{{< /highlight >}}<p>These are all the options you can specify:</p>

{{< highlight "bash" "style=default" >}}<![CDATA[

SVN_BASE=''

SVN_PREFIX=''

SVN_SUFFIX=''

VFS_BASE=''  

VFS_PREFIX=''

VFS_SUFFIX=''



DEFAULT_REPO_TYPE='vfs'

ALLOWED_REPO_TYPES='vfs'

IGNORE_DATASET_REMOTE_SVN=0 #nag if the repo url figured out is not the same as the one in 'svn info'. you should leave this 0

]]>{{< /highlight >}}<h5>dataset/.ddm</h5>

<p>For an example see below.  Possible options are these:</p>

{{< highlight "bash" "style=default" >}}<![CDATA[

DATASET_LOCAL='' #path to dataset locally (including type suffix if any)

DATASET_REMOTE='' #path to dataset remotely (or locally if network mount)

DATASET_PATH='' #just the path (until parent directory of dataset)

DATASET_DIR_NAME='' #like $DATASET_LOCAL but no path 

DATASET_DIR_NAME_REL  # identifier to dataset, taken against pwd ( could be '.','..', nothing at all, dirname, full path, ..)

DATASET_NAME='' #like $DATASET_DIR_NAME but no type suffix

DATASET_TYPE=''

REPO_TYPE=''



#you can override the following callbacks (example see below)

precheckout

docheckout

postcheckout



precommit

docommit

postcommit



preupdate

doupdate

postupdate

]]>{{< /highlight >}}<h4>Invocation</h4>

<pre><![CDATA[

dieter@dieter-mbp:~$ ddm -h

usage: ddm options



OPTIONS:

   -d                Dataset (name of directory)

   -h                Show this message

   -m                Message (used for commits in svn, ignored otherwise)

   -u                Update

   -c                Commit

   -o                Checkout (default repo type)

   -O <repo-type>    Checkout using specific repo type (one of: svn vfs)

   -t <dataset-type> Specify dataset-type (selection,copy, ...) (only honoured for checkouts)

   -v                Verbose

]]></pre><h4>Examples</h4>

<h5>Update my video-selection.</h5>

<p>The directory is ~/video-selection.  It contains episodes that I'm watching<br />

The .ddm file looks like this</p>

{{< highlight "bash" "style=default" >}}<![CDATA[

doupdate()

{

	slidewindow mplayer 10 1

}

]]>{{< /highlight >}}<p>This means that ddm will look in my bash history and look for the movie files in this directory I have played (using "mplayer video-selection/*somefile*).<br />

It will then delete all the ones I've already seen, except the latest one (parameter 3). It will also fetch the next 10 episodes (parameter 2)</p>

<pre><![CDATA[

dieter@dieter-mbp:~$ ddm -u -v -d video-selection/

Included /home/dieter/video-selection/.ddm

action update on dataset name video type selection

Deleting old files... (3 items).

 * /home/dieter/video-selection/910 - The One With Christmas In Tulsa.avi... success

 * /home/dieter/video-selection/911 - The One Where Rachel Goes Back To Work.avi... success

 * /home/dieter/video-selection/912 - The One With Phoebes Rats.avi... success

Keeping these files... (1 items).

 * /home/dieter/video-selection/913 - The One Where Monica Sings.avi

Copying new files... (10 items).

 * /home/dieter/video-selection/914 - The One With The Blind Dates.avi... success

 * /home/dieter/video-selection/915 - The One With the Mugging.avi... success

 * /home/dieter/video-selection/916 - The One With The Boob Job.avi... success

 * /home/dieter/video-selection/917 - The One With The Memorial Service.avi... success

 * /home/dieter/video-selection/918 - The One With The Lottery.avi... success

 * /home/dieter/video-selection/919 - The One With Rachels Dream.avi... success

 * /home/dieter/video-selection/920 - The One With The Soap Opera Party.avi... success

 * /home/dieter/video-selection/921 - The One With The Fertility Test.avi... success

 * /home/dieter/video-selection/922 - The One With The Donor.avi... success

 * /home/dieter/video-selection/923 - 924 - The One In Barbados.avi... success

finished

]]></pre><h4>Download</h4>

<p>The code is licensed under <a href="http://www.gnu.org/licenses/gpl-3.0.txt">Gpl v3</a><br />

You can dowload it <a href="/files/ddm" onClick="javascript:urchinTracker ('/files/ddm');">here</a></p>
