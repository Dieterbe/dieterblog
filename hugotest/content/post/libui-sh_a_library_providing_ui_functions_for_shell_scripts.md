+++
title = "Libui-sh: a library providing UI functions for shell scripts"
date = "2010-12-28T22:59:15-04:00"
tags = ["foss", "bash"]
+++
== A library providing UI functions for shell scripts ==</p>

<p>When you write bash/shell scripts, do you write your own error/debug/logging/abort functions?<br />

Logic that requests the user to input a boolean, string, password, selection out of a list,<br />

date/time, integer, ... ?</p>

<p>Libui-sh is written to take care of all that.<br />

libui-sh is meant to a be a general-purpose UI abstraction library for shell scripts.<br />

Low impact, easy to use, but still flexible.<br />

cli by default, can optionally use ncurses dialogs as well.<br />

<!--more--></p>

<p>To start using it, you only need to source it and you can start calling its functions.<br />

To reconfigure it (i.e. to change UI type, debug settings, logfile location),<br />

just run the command libui_sh_init</p>

<p>example usage:</p>

{{< highlight "bash" "style=default" >}}<![CDATA[

source /usr/lib/libui.sh

ask_yesno 'do you want to continue?' || return

libui_sh_init cli /tmp /tmp/yourlogfile

log 'we just got hassle-free logging'

]]>{{< /highlight >}}<p>

The library is not strictly a UI library, it also contains a few useful functions like<br />

check_is_in (check if an element can be found in a set - usually an array) and<br />

seteditor (interactive $EDITOR selection)</p>

<p>Dependencies:<br />

- bash (for cli interface)<br />

- optionally: dialog (for ncurses interface)

</p></blockquote>

<p><a href="https://github.com/Dieterbe/libui-sh">https://github.com/Dieterbe/libui-sh</a></p>
