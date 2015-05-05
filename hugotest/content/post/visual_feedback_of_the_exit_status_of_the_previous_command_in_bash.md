+++
title = "Visual feedback of the exit status of the previous command in bash"
date = "2008-10-14T21:56:50-04:00"
tags = ["bash"]
+++
{{< highlight "bash" "style=default" >}}<![CDATA[

if [ $(tput colors) -gt 0 ] ; then

    RED=$(tput setaf 1)

    GREEN=$(tput setaf 2)

    RST=$(tput op)

fi



bash_prompt_command() {

        last_exit=$?

        exit_to_color=$RED

        [ $last_exit == 0 ] && exit_to_color=$GREEN

}



export PROMPT_COMMAND=bash_prompt_command



PS1="\u@\h \[\$exit_to_color\]\W\[$RST\] \$"

]]>{{< /highlight >}}<p>

( Inspired by <a href="http://bbs.archlinux.org/viewtopic.php?pid=367626#p367626">this post</a> )</p>
