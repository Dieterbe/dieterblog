+++
title = "A script that pulls photos from facebook"
date = "2009-08-18T17:36:21-04:00"
tags = ["bash"]
+++
<p><a href="http://fbcmd.dtompkins.com/">Fbcmd</a> is pretty cool.<br />

I quickly hacked this script together which pulls all photo albums from friends on facebook, so I have them available where I want.  (It should also pull your own albums, but I don't have any so I can't check that)<!--more--><br />

Maybe there are better ways to do this.  I looked at <a href="http://nerd256.diggles.net/fbfs/">fbfs</a> but it looks a bit weird.  I have no idea what the corrupted images fuss is all about.</p>

{{< highlight "bash" "style=default" >}}<![CDATA[

#!/bin/bash



dir=$HOME/fbphotos

cache=${XDG_CACHE_HOME:-$HOME/.cache}

[ -d $cache ] || mkdir $cache

[ -d $cache ] || exit 2

#fbcmd=`which fbcmd`

fbcmd='php /home/dieter/fbcmd/fbcmd.php'



echo "Fetching info about friends and myself .."

$fbcmd FRIENDS -csv | tail -n '+2' > $cache/fb-users # ID NAME

$fbcmd WHOAMI  -csv >> $cache/fb-users



while read line

do

        uid=`  cut -d ',' -f 1 <<< "$line"`

        uname=`cut -d ',' -f 2 <<< "$line"`

        echo "Fetching list of albums for user $uname ... "

        $fbcmd ALBUMS $uid -csv | tail -n '+2' > $cache/fb-$uid-albums #OWNER_NAME AID NAME SIZE

done < $cache/fb-users



for i in $cache/fb-*-albums

do

        while read line

        do

                oname=`cut -d ',' -f 1 <<< "$line"`

                aid=`  cut -d ',' -f 2 <<< "$line"`

                aname=`cut -d ',' -f 3 <<< "$line"`

                asize=`cut -d ',' -f 4 <<< "$line"`

                echo "Fetching $oname album: $aname"

                $fbcmd APICS $aid $dir -psize=1 -af="$oname-$aname/[pid].jpg" -pic_skip_exists=1

        done < $i

done

]]>{{< /highlight >}}<p>

Here's a picture from <a href="http://www.countingcows.be">Counting cows</a> I grabbed from <a href="http://lievendekeyser.net/">Lievens</a> album.<br />

<img src="/files/countingcows2009.jpg" /></p>
