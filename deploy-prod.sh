#!/bin/bash
echo ">>>>> build"
rm -rf pub/public-prod
hugo --config config-prod.toml -d pub/public-prod
rsync -a --delete files/ pub/public-prod/files/
echo ">>>>> deploy"
rsync -a --delete pub/public-prod/ arch1:/srv/http/dieter/
