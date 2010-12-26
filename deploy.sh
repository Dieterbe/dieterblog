#!/bin/bash

function usage () {
	echo "Blog deployment script"
	echo "\$1 : a directory where to deploy, like /srv/http/myblog"
	echo "\$2 : a base url to configure (optional), eg: \"http://www.example.com/weblog\""
	echo "\$3 : 1 to also update comments"
}

if [ "$1" = '-h' -o "$1" = '--help' ]
then
	usage
	exit 0
fi

src=`dirname "$0"`
if [ ! -f $src/blog.tpl.ini ]
then
	echo "$src/blog.tpl.ini not found! Not deploying" >&2
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

echo -n "Deploying to $dst..."
if [ "$3" != 1 ]
then
	cmd='rsync -au --delete --exclude=/entries/comments/*'
	echo "leaving comments intact."
else
	cmd='rsync -au --delete'
	echo "updating comments as well"
fi
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

if [ -n $2 ]
then
	if ! sed -i "s#.*base_url.*=.*__BASE_URL__.*#py[\"base_url\"] = \"$2\"#" $dst/config.tpl.py
	then
		echo "Could not set base_url to $2 in $dst/config.tpl.py" >&2
		exit 2
	fi
fi

echo "Correctly naming now-expanded config templates..."
if ! mv $dst/config.tpl.py $dst/config.py
then
	echo "Could not mv $dst/config.tpl.py $dst/config.py"
	exit 2
fi
if ! mv $dst/blog.tpl.ini $dst/blog.ini
then
	echo "Could not mv $dst/blog.tpl.ini $dst/blog.ini"
	exit 2
fi

echo "Generating tags.."
if ! pyblosxom-cmd buildtags --config=$dst/config.py
then
	echo "Could not pyblosxom-cmd buildtags --config=$dst/config.py" >&2
	exit 2
fi

# TODO: not for every distro/use-case.  might want to make this configurable
echo "Fixing ownerships of $dst.."
if ! chown -R http.http $dst
then
	echo "Could not chown -R http.http $dst" >&2
	exit 2
fi
