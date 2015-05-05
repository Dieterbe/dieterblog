+++
title = "gtk dialogs for (shell)scripts with zenity and the ask-pass gui tools for ssh-add"
date = "2007-11-25T18:45:41-04:00"
tags = ["foss", "bash"]
+++
<p>Phew! where to start?  Probably at <a href ="http://www.chimeric.de/blog/2007/1107_mounting_external_truecrypt_volumes_interactively">this blogpost</a>.  It's about making it very easy to work with external encrypted volumes. I'm not going to talk about the article itself but about a great tool i discovered thanks to it: Zenity. <!--more--> It's an LGPL-licensed program written in C by some guys from Gnome and Sun. You can call it from any script and present a user with a gtk widget such as a password-dialog, filechooser, calendar, ... It has <a href="http://www.linuxmanpages.com/man1/zenity.1.php">many possibilities</a>.<br />

This is great if you want to run scripts on the terminal or even without a terminal (scripts automatically started by your desktop environment) and need user input.</p>

<p>This immediately made me think of using this together with ssh-add, because i was getting a bit tired to open a console and add my key by typing the ssh-add command for every X session. (For the record: ssh-add without any arguments is enough for most users: it looks for keys with default names, but i have multiple keys with some speial names so...)<br />

(I can easily retrieve the right command by typing ssh-add*arrowup* but still it's cumbersome.. see <a href="/my_favorite_bash_tricks">this page for the bash-trick</a>)</p>

<p>Of course I realized I was probably not the only one with this idea so I googled a bit and looked in the <a href="http://www.hmug.org/man/1/ssh-add.php">ssh-add manpage</a>, and I found out some cool stuff!<br />

It turned out ssh-add has support for such scenarios and offers the $SSH_ASKPASS environment variable for this.  Since the system I'm currently using on my laptop (which i converted from Arch to xubuntu 7.10 but that's another story :-)) doesn't have this variable set by default I could of course set it myself, but it can be even easier then this...</p>

<p>When the $SSH_ASKPASS variable is not set, ssh-add will try to execute /usr/bin/ssh-askpass by default.  I figured this out by typing this in a console:<br />

ssh-add *mykey* < /dev/null<br />

This revealed that there are already some utilities specifically for this purpose!  Let's see...:</p>

<pre><![CDATA[

dieter@dieter-mbp:~$ aptitude search askpass

p   gtk-led-askpass                                                - GTK+ password dialog suitable for use with ssh-add                      

p   ssh-askpass                                                    - under X, asks user for a passphrase for ssh-add                         

p   ssh-askpass-fullscreen                                         - Under Gnome2, asks user for a passphrase for ssh-add                    

p   ssh-askpass-gnome                                              - interactive X program to prompt users for a passphrase for ssh-add  

]]></pre><p>I decided to install ssh-askpass-gnome even though I use xfce.  And it works great :D</p>

<p>After installing this you can just put your ssh-add line in the settings panel called "autostarted Applications" from Xfce and for your next session it will show a nice gtk popup to ask for your password and it works like a charm :)<br />

However, since i use multiple keys, i used to use the globbing operator (*) but this doesnt work anymore with this method.  I guess that makes sense as the globbing operator is probably a bash built-in...</p>
