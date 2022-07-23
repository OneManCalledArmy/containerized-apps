#!/bin/bash

cd /home/jacek/app-system/consumer

docker build . -t consumer:v1.0.0
docker run -it --rm --network real_devops_sht -e RABBIT_HOST=rabbit-manager -e RABBIT_PORT=5672 -e RABBIT_USERNAME=guest -e RABBIT_PASSWORD=guest -p 80:5000 --name producer producer:v1.0.0