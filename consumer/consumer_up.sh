#!/bin/bash

cd /home/jacek/containerized-apps/consumer
# cd /consumer

docker build . -t consumer:v1.0.0
docker run --network real_devops_sht -e REDIS_HOST=redis-sys -e REDIS_PORT=6379 -e RABBIT_HOST=rabbit-manager -e RABBIT_PORT=5672 -e RABBIT_USERNAME=guest -e RABBIT_PASSWORD=guest --name consumer consumer:v1.0.0

# cd ..