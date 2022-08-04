#!/bin/bash

cd /home/jacek/containerized-apps/testground

docker build . -t tester:v1.0.0
docker run -e test-key=test-value -p 5000:5000 --name tester onemancalledarmy/tester:v1.0.0


# cd ..