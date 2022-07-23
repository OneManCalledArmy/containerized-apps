#!/bin/bash

docker network create --driver bridge real_devops_sht

docker run -d --rm --net real_devops_sht --hostname crazy-rabbit --name crazy-rabbit rabbitmq:3.8

# docker rm -f crazy-rabbit

docker run -d --rm --net real_devops_sht -p 8080:15672 --hostname rabbit-manager --name rabbit-manager rabbitmq:3.8-management

# docker exec -it rabbit-manager rabbitmqctl stop_app
# docker exec -it rabbit-manager rabbitmqctl reset
# docker exec -it rabbit-manager rabbitmqctl join_cluster rabbit@rabbit-1
# docker exec -it rabbit-manager rabbitmqctl start_app
# docker exec -it rabbit-manager rabbitmqctl cluster_status

docker exec -it crazy-rabbit rabbitmq-plugins enable rabbitmq_management