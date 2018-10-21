#!/usr/bin/env sh
set -e

python main.py dsm.tif result.json 100 &
jobs
echo $!
psrecord $! --interval 1 --log mem.log
cat mem.log

set +e
