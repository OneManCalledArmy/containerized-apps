#!/bin/bash

cd /home/jacek/containerized-apps/sizer
# cd /sizer

docker build . -t sizer:v1.0.0
docker run --network real_devops_sht -e REDIS_HOST=redis-sys -e REDIS_PORT=6379 -p 5000:5000 --name sizer sizer:v1.0.0

# cd ..