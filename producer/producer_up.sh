#!/bin/bash

cd /home/jacek/containerized-apps/producer
# cd /producer

docker build . -t producer:v1.0.3
docker run --network real_devops_sht -e RABBIT_HOST=rabbit-manager -e RABBIT_PORT=5672 -e RABBIT_USERNAME=guest -e RABBIT_PASSWORD=guest -p 80:5000 --name producer producer:v1.0.3
# cd ..