#TODO:
run containers as non-root users
https://stackoverflow.com/questions/27701930/how-to-add-users-to-docker-container

change to specific namespace


APP:
---
Build image:
cd
docker build . -t onemancalledarmy/tag

Push image:
docker push onemancalledarmy/tag

Deployment:
kubectl apply -f foldername/deployment/deployment.yaml

Service:
kubectl apply -f 

Producer:
---
Build image:
cd producer
docker build . -t onemancalledarmy/producer-python:v1.0.4

Push image:
docker push onemancalledarmy/producer-python:v1.0.4

Deployment:
kubectl apply -f producer/deployment/deployment.yaml

Service:
kubectl apply -f producer/service/service.yaml

Consumer:
---
Build image:
cd consumer
docker build . -t onemancalledarmy/consumer-python:v1.0.1

Push image:
docker push onemancalledarmy/consumer-python:v1.0.1

Deployment:
kubectl apply -f consumer/deployment/deployment.yaml

Sizer:
---
Build image:
cd sizer
docker build . -t onemancalledarmy/sizer-python:v1.0.2

Push image:
docker push onemancalledarmy/sizer-python:v1.0.2

Deployment:
kubectl apply -f sizer/deployment/deployment.yaml

Service:
kubectl apply -f sizer/service/service.yaml

Nginx
---
kubectl apply -f nginx/deployment/deployment.yaml

Redis:
---

kubectl apply -f sc.yaml

kubectl apply -f pv.yaml

kubectl apply -n default -f redis-config.yaml

kubectl apply -n default -f redis-statefulset.yaml

kubectl apply -n default -f redis-service.yaml

RabbitMq:
---
kubectl apply -n default -f .\kubernetes\rabbit-rbac.yaml
kubectl apply -n default -f .\kubernetes\rabbit-configmap.yaml
kubectl apply -n default -f .\kubernetes\rabbit-secret.yaml
kubectl apply -n default -f .\kubernetes\rabbit-statefulset.yaml