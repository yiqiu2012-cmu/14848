## Apache Hadoop
### Prepare docker compose
- `nano docker-compose.yml`
- Copy `docker-compose.yml` from https://github.com/big-data-europe/docker-hadoop
### Download Kompose and convert docker-compose.yml file to files that can run with `kubectl`
- `curl -L https://github.com/kubernetes/kompose/releases/download/v1.24.0/kompose-linux-amd64 -o kompose`  
`chmod +x kompose`
`sudo mv ./kompose /usr/local/bin/kompose`
`kompose convert`
- `kompose convert` would return a list of files that can be built by kubectl. 
- Run `kubectl` on the list files returned
### CHek service and pods
- `kubectl get pods`
- `kubectl get svc`
