## Build docker image

docker build -t yiqiu2012/toolbox_ui .

## Push docker image to Dockerhub

docker push yiqiu2012/toolbox_ui

### Pull images from docker hub and push to container registry

- docker pull yiqiu2012/
- docker tag yiqiu2012/toolbox_ui gcr.io/<Porject ID>/yiqiu2012/toolbox_ui
- docker push gcr.io/<Porject ID>/yiqiu2012/toolbox_ui

### Pull image from container registry

- docker pull yiqiu2012/toolbox_ui

### Compose yaml file

- nano toolbox_deployment.yaml
- nano toolbox_service.yaml
  Copy from existing yaml file from my github

### Deploy using kubectl

- kubectl apply -f toolbox_deployment.yaml
- kubectl apply -f toolbox_service.yaml

### Check pods and service

- kubectl get pods
- kuebctl get svc
