#!/bin/bash

function usage () {
	echo "Remote (other host) blog deployment script."
	echo "copies to private dir first on remote host first, then invokes deploy script on remote host"
	echo "\$1 : rsync-format location to submit content to (not public) (like somehost:mycode/blog)"
	echo "shift; \$@ : args for deploy.sh script"
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
host=$(echo "$dst" | cut -d: -f1)
dir=$(echo "$dst" | cut -d: -f2)
echo "Assuring directory $dir existence on $host"
if ! ssh $host "mkdir -p $dir"
then
	echo "could not assure existence of $dir on $host"
	exit 2
fi
echo "Submitting files to $dst..."
if ! rsync -a --delete "$src/" "$dst/"
then
	echo "Could not submit $src to $dst" >&2
	exit 2
fi
shift
echo -n "Deploying on $host: sudo $dir/deploy.sh $@..."
if ! ssh $host "sudo $dir/deploy.sh $@"
then
	echo "Remote deploy failed"
	exit 2
fi
echo "Remote deploy done"
exit
