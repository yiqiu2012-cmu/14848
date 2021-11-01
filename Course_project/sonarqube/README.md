### Pull images from docker hub and push to container registry
- docker pull yiqiu2012/sonarqube 
- docker tag yiqiu2012/sonarqube gcr.io/<Porject ID>/yiqiu2012/sonarqube
- docker push gcr.io/<Porject ID>/yiqiu2012/sonarqube

### Pull image from container registry
- docker pull yiqiu2012/sonarqube 

### Compose yaml file
- nano sonarqube_deployment.yaml
- nano sonarqube_service.yaml
Copy from existing yaml file from my github

### Deploy using kubectl
- kubectl apply -f sonarqube_deployment.yaml
- kubectl apply -f sonarqube_service.yaml

### Check pods and service
- kubectl get pods
- kuebctl get svc 