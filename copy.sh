#!/usr/bin/env sh
set -e

docker cp ./*.py dsm-to-elevation-array:/home/dsm-to-elevation-array
docker cp dsm.tif dsm-to-elevation-array:/home/dsm-to-elevation-array

set +e
