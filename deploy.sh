#!/bin/bash

function usage () {
	echo "Blog deployment script"
	echo "\$1 : a directory where to deploy, like /srv/http/myblog"
}

if [ "$1" = '-h' -o "$1" = '--help' ]
then
	usage
	exit 0
fi

src=`dirname "$0"`
if [ ! -f $src/blog.ini ]
then
	echo "$src/blog.ini not found! Not deploying" >&2
	exit 2
fi

[ -z $1 ] && usage && exit 2
dst="$1"

echo "(Maybe) creating $dst..."
if ! mkdir -p "$dst"
then
	echo "Could not create $dst" >&2
	exit 2
fi

echo "Deploying to $dst..."
cmd='rsync -au --delete'
if ! $cmd $src/ $dst/
then
	echo "Could not $cmd $src/ $dst/"
	exit 2
fi

# TODO: this is racey, maybe do it in separate dir first and then do a mv
echo "Configuring $dst..."

find $dst -type f | grep -v '\.git' | xargs sed -i "s#__DEPLOYDIR__#$dst#g"
find_exit=${PIPESTATUS[0]}
sed_status=$?
if [ $find_exit -gt 0 -o $sed_status -gt 0 ]
then
	echo "Something failed" >&2
	echo "Find exitcode: $find_exit" >&2
	echo "Sed  exitcode: $sed_exit" >&2
	exit 2
fi

# TODO: not for every distro/use-case.  might want to make this configurable
echo "Fixing ownerships of $dst.."
if ! chown -R http.http $dst
then
	echo "Could not chown -R http.http $dst" >&2
	exit 2
fi
