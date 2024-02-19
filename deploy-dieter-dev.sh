#!/bin/bash
echo ">>>>> build"
hugo --config config-dieter-dev.toml -d pub/public-dieter-dev
echo ">>>>> rsync html"
rsync -a --delete pub/public-dieter-dev/ arch1:/srv/http/dieter-dev/
echo ">>>>> rsync files"
rsync -a --delete files-from-octo-dontchange/ arch1:/srv/http/files/
