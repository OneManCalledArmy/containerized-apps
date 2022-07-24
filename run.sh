#!/bin/bash /path/to/script

# REDIS_HOST=redis-sys
# REDIS_PORT=6379
# RABBIT_HOST=rabbit-manager
# RABBIT_PORT=5672
# RABBIT_USERNAME=guest
# RABBIT_PASSWORD=guest

docker network create --driver bridge real_devops_sht

./rabbit/rabbit_up.sh
./redis/redis_up.sh
./producer/producer_up.sh
./consumer/consumer_up.sh
./sizer/sizer_up.sh