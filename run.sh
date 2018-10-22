#!/usr/bin/env sh
set -e

docker start dsm-to-elevation-array
docker exec dsm-to-elevation-array python main.py dsm.tif result.json 100
docker stop dsm-to-elevation-array

set +e
