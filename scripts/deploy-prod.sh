#!/bin/bash
echo ">>>>> build"
d=pub/public-prod-$(date +'%Y-%m-%d_%H-%M-%S')
echo "dir: $d"
hugo --config config-prod.toml -d $d
rsync -a --delete files/ $d/files/
echo ">>>>> deploy"
rsync -a --delete $d/ arch1:/srv/http/dieter/
