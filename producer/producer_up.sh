#!/bin/bash

# cd /home/jacek/containerized-apps/producer
cd /producer

docker build . -t producer:v1.0.0
docker run -it --rm --network real_devops_sht -e RABBIT_HOST=rabbit-manager -e RABBIT_PORT=5672 

cd ..