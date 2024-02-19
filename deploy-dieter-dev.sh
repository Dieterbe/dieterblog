#!/bin/bash
echo ">>>>> build"
hugo --config config-dieter-dev.toml -d pub/public-dieter-dev
rsync -a --delete files/ pub/public-dieter-dev/files/
echo ">>>>> deploy"
rsync -a --delete pub/public-dieter-dev/ arch1:/srv/http/dieter-dev/
