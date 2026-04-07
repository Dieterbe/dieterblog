#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for d in pub/public-dieter-dev*; do
  echo "> $d"
  $SCRIPT_DIR/compare-pub.sh pub/public-prod $d | wc -l
done
