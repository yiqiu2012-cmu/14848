### Pull images from docker hub and push to container registry
- docker pull yiqiu2012/jupyter 
- docker tag yiqiu2012/jupyter gcr.io/<Porject ID>/yiqiu2012/jupyter
- docker push gcr.io/<Porject ID>/yiqiu2012/jupyter

### Pull image from container registry
- docker pull yiqiu2012/jupyter 

### Compose yaml file
- nano jupyter_deployment.yaml
- nano jupyter_service.yaml
Copy from existing yaml file from my github

### Deploy using kubectl
- kubectl apply -f jupyter_deployment.yaml
- kubectl apply -f jupyter_service.yaml

### Check pods and service
- kubectl get pods
- kuebctl get svc 