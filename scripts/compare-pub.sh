#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source $SCRIPT_DIR/lib.sh
d1=$1
d2=$2
if [ ! -d "$d1" ] || [ ! -d "$d2" ]; then
  echo "Usage: $0 <dir1> <dir2>"
  exit 1
fi
d1norm=$(mktemp -d -t "$(basename "$d1")-norm.XXXXXX")
d2norm=$(mktemp -d -t "$(basename "$d2")-norm.XXXXXX")
$SCRIPT_DIR/copy-normalized.sh "$d1" "$d1norm"
$SCRIPT_DIR/copy-normalized.sh "$d2" "$d2norm"

compare "$d1norm" "$d2norm"

