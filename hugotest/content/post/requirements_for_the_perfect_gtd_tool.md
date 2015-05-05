+++
title = "Requirements for the perfect GTD tool"
date = "2008-08-09T16:04:45-04:00"
tags = ["life", "productivity", "foss"]
+++
<p>I've been reading <a href="http://en.wikipedia.org/wiki/Getting_Things_Done">GTD</a> lately and it's absolutely a great and inspiring book.<br />

Having made my home office space into a real <i>Zen</i> I want to start implementing GTD in my digital life but it seems very hard to find a good GTD tool that fully implements GTD. (even though there are a lot of tools out there)</p>

<p>The most interesting ones (each for different reasons) I've looked at so far are <a href="http://www.thinkingrock.com.au/index.php">Thinkingrock</a>, <a href="http://www.rousette.org.uk/projects/">tracks</a> and <a href="https://gna.org/projects/yagtd/">yagtd</a> (the latter requiring most work before it does everything I need, but it's also the most easy to dive into the code base). I'm keeping my eyes open because there are certainly more things to discover.</p>

<p>Even though there are probably no applications out there that can do everything I want, I just wanted to share my feature-wishlist.  These are the requirements I find that a really good tool should comply with:<br />

<!--more--><br />

In order of importance (sort of):</p>

<ul>

<li><i>I want to have control over both my data and application.</i><br />

 At least half of the GTD apps out there are websites ran by an external party.  I want to run the application myself, I must have access to the source code, and I want to have my data myself.</li>

<li><i>Rapid idea collection and processing.</i><br />

  David Allen mentions the importance of this several times.  Sometimes you are doing something but come up with something else which you want to write down to continue your other stuff as quickly as you can.  Later on - in 'processing mode' - these notes must be handled one by one, and it must be easy to choose whether you want to create a new task from this note, throw it away, file/further edit as a note for something else and so on.  For some reason many GTD applications skip these very important collection and processing steps and assume their users will enter actions right away.  For now I've only seen Thingkingrock handling this nicely (or at all).  A workaround could be to use a notes-taking application such as tomboy as collection bucket, and process that every once in a while but then you'll need to copy-paste stuff from one application into another etc.  Doable but cumbersome and avoidable.</li>

<li><i>Context / project editors</i><br />

Context and projects are entities on their own. I don't want any of them disappearing/non-existing just because there are no actions that 'link to them' anymore/yet.  (which seems to be the case with yagtd).  Tracks handles this really nicely.</li>

<li><i>Advanced reference system.</i><br />

Notes/documentation (with documentation I don't mean physical files such as *.pdf or *.odt but just textual data) must be able to get filed and easily be retrieved by itself or by associated item.  A note should be able to be linked to an action or project but must also be able to stand on it's own through it's title and/or a tagging system.  Some notes can even be related to multiple projects/actions (from different projects).  In many cases I find it useful to link a project to one or more notes who are already general reference material or linked to something else.  So this goes <i>way</i> beyond the simple 'description' fields that most tools offer.  Support for holding not only text, but also hyperlinks, images, movie clips, would be a plus. (not the most important though)</li>

<li><i>File format</i><br />

An easily accessible file format is a plus for a variety of reasons.  Plaintext is the winner here (yagtd).  Tracks does not seem to support a plaintext backend but it does support an api/rss/.. and an export feature so that counts too.  ThinkingRock uses xml. (mixed feelings about that)

</li>

<li><i>action/project dependencies</i><br />

Some actions or projects can't be done at all as long as another project or action is not finished.  If you can specify this in your program, than the program can put the action/project in the 'waitingfor' section and move it  to 'next actions' when the dependencies are fulfilled. (after asking confirmation maybe)</li>

<li><i>Calendar integration</i><br />

A full featured calender does not belong in a GTD tool, ( because on a calender you also want to put non-actionable stuff like certain events, birthdays,...) but there does need to be support for exporting everything with a date on it (actions with due dates or that can only happen on specific moments each week/day/...) to a calendar.  Ical is probably the most common for this, but with an rss feed or rest api I can help myself too. (by converting it into ical or whatever)</li>

<li><i>project planning on the beforehand</i><br />

When planning a project you already know more action steps then just the next one for a project.  If you can specify these in a good way (e.g. not by abusing the project description field) the program can open the next action when you complete the current one.</li>

<li><i>Reminders</i><br />

I want to be informed automatically of stuff that *needs* to happen.  Gtk or libnotify popups are great, e-mail will do too.  Being able to respond to the notification to say 'inform me again at $foo' or 'i just did this, close the action!' are a plus.

</li>

<li><i>History</i><br />

When did I do this? What happened to item X at this date?  Questions that sometimes need an answer and it's frustrating if you don't have them.</li>

<li><i>GTD on the road</i><br />

I can use a paper notebook for collecting ideas and for quickly writing some reminders down before closing the laptop but having access to my GTD data on my phone would be really nice. (preferably by syncing the phone with my laptop to be not dependent on a network at all times) (I will be having an iphone soon)

</li>

<li><i>Integration with email</i><br />

How great would be to specify in your GTD tool 'this action is waiting for John Doe' and later, when you receive a mail from John Doe you can say 'this closes this action' ?  Or for each mail in your inbox you have some options to import the contents into your collection bucket, into a new task or into the filing system?  Practically how this could work is through an api like what tracks offers, or by dbus for desktop programs.

</li>

</ul>

<h3>About the book</h3>

<p>GTD has received a lot of hype, which made me sceptical at first but while reading the book it became clear the praise is deserved.<br />

Right from the beginning you start learning many things, and throughout the book the 'eureka' moments keep coming.  Even I who have been thinking quite a lot on how to organize my todo's, ideas and reference material am surprised by how much can be improved.  There are some points that are not new and are also mentioned in other time management books (such as 'getting a clear head') but the great part is that GTD is not only about action management, but also about project planning, personal organisation, how to manage those ideas/questions/reminders that you come up with randomly, office organisation and so on. I was afraid that some things I do/need would not be handled in the book but it's definitely not the case.  And everything is handled both in theory and in practice with a lot of thoughts, ideas and practical recommendations.  David's advice after more then 20 years of productivity consulting/training/research is something that no-one should miss.<br />

From a writers perspective: I find it also amazing how stuff that is so hard to explain is so well organized and explained in a easy to understand phrasing throughout the entire book.  Not that I know much about this field but it's clear that this part of the book also has gotten a lot of work.  In a few rare cases I found that some recommendations were not backed up enough but those were just details.</p>

<p>While reading the book (I haven't finished it yet btw) I spent several days cleaning up my room.  I started using a filing cabinet for my reference material (placed very accessibly!), organized supplies and equipment on my desk etc etc.  There is still some work to do but on the short term I want to have gotten rid of everything I don't need, and keep what I need in the places that make most sense for them, and in the end I want to know where everything is (so I never need to search) and there should be nothing where it doesn't belong...</p>

<p>My parents had to stop me from starting to clean up our entire attic...  This book definitely has changed me.  (those who know how I used to leave my stuff will understand ;-)</p>
