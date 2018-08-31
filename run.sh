docker start dsm-to-elevation-array
docker exec dsm-to-elevation-array python main.py dsm.tif result.json
docker stop dsm-to-elevation-array
