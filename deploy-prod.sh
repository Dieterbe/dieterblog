#!/bin/bash
echo ">>>>> build"
hugo --config config-prod.toml -d pub/public-prod
echo ">>>>> rsync html"
rsync -a --delete pub/public-prod/ arch1:/srv/http/dieter/
echo ">>>>> rsync files"
rsync -a --delete files-from-octo-dontchange/ arch1:/srv/http/files/
