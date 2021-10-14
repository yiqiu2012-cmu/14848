step 1: push container to docker hub

1.1
cd sa-frontend
docker build -f Dockerfile -t yiqiu2012/sentiment-analysis-frontend .
docker push yiqiu2012/sentiment-analysis-frontend
1.2
cd ../sa-logic
docker build -f Dockerfile -t yiqiu2012/sentiment-analysis-logic .
docker push yiqiu2012/sentiment-analysis-logic
1.3
cd ../sa-webapp
docker build -f Dockerfile -t yiqiu2012/sentiment-analysis-webapp .
docker push yiqiu2012/sentiment-analysis-logic

step 2: create project on GCP, enable billing and container registry API

step 3: pull image from dockerhub and push to cloud container registry
docker pull yiqiu2012/sentiment-analysis-frontend
docker tag yiqiu2012/sentiment-analysis-frontend gcr.io/extra-credit-mini/yiqiu2012/sentiment-analysis-frontend:latest
docker pull yiqiu2012/sentiment-analysis-logic
docker tag yiqiu2012/sentiment-analysis-frontend gcr.io/extra-credit-mini/yiqiu2012/sentiment-analysis-frontend:latest
docker pull yiqiu2012/sentiment-analysis-webapp
docker tag yiqiu2012/sentiment-analysis-frontend gcr.io/extra-credit-mini/yiqiu2012/sentiment-analysis-frontend:latest

step 4: create cluster using GCP console

step 5: create deployment and loadbalancer service for frontend and webapp using yaml files in resource-manifests
kubectl apply -f sa-frontend-deployment.yaml
kubectl create -f service-sa-frontend-lb.yaml
kubectl apply -f sa-web-app-deployment.yaml
kubectl apply -f service-sa-web-app-lb.yaml

step 6: create deployment and service for logic to communicate with web app
kubectl apply -f sa-logic-deployment.yaml
kubectl apply -f service-sa-logic.yaml

step 7: change the ip in sa-frontend/src/App.s to Extermanl IP:PORT and redeploy the docker image
step 8: on GCP cloud shell, pull the image and re-deploy using yaml
