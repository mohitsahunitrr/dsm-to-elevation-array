#!/usr/bin/env sh
set -e

docker build . -t dsm-to-elevation-array
docker create -it --name dsm-to-elevation-array dsm-to-elevation-array

set +e
