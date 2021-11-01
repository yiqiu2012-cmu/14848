Used bitnami/spark image and helm charts for deployment

- within kubernetes cluster on GKE, run 
$ helm repo add bitnami https://charts.bitnami.com/bitnami
- Set up service as loadbalancer to allow access to application through external IP 
$ helm install bitnami/spark --set service.type=LoadBalancer
- kubectl get pods
- kubetl get svc
 