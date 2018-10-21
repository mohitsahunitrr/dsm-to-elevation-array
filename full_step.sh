#!/usr/bin/env sh
set -e

docker cp ./*.py dsm-to-elevation-array:/home/dsm-to-elevation-array
docker cp dsm.tif dsm-to-elevation-array:/home/dsm-to-elevation-array
docker start dsm-to-elevation-array
docker exec dsm-to-elevation-array python main.py dsm.tif result.json 100
docker cp dsm-to-elevation-array:/home/dsm-to-elevation-array/result.json .
docker stop dsm-to-elevation-array

set +e
