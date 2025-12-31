- the auth service docker file needs some updates, refer in this repo
- `docker build -t gokulkris/auth_service:latest .`use this command to tag your image

- `docker push gokulkris/auth_service:latest` to push we need to login to docker hub

- `docker login` to login to docker hub or `docker login -u gokulkris`

- to tag an image use `docker tag <local_image_id> gokulkris/auth_service:latest`
 
- how to run k9s in ubuntu
    - `sudo snap install k9s` to install k9s
    - `k9s` to run k9s 


- `kubectl apply -f ./` this in the manifests folder to apply all the manifests
    - this will create all the deployments and services in the kubernetes cluster and you can check using `kubectl get pods` and `kubectl get services`


- in case you make an update in code, you need to rebuild the docker image and push it to docker hub again and then you can do a rolling update in kubernetes using the command below
    - `kubectl set image deployment/<deployment_name> <container_name>=<new_image_name>:<tag>` example `kubectl set image deployment/auth-deployment auth-service=gokulkris/auth_service:latest`
    - this will do a rolling update of the deployment with zero downtime

- `cd /home/gokul/gokul_repos/go_microservice_project_1/system_design/pythonn/src/gateway/manifests && kubectl apply -f gateway-deploy.yaml && kubectl rollout restart deployment/gateway && kubectl rollout status deployment/gateway`

- to redeploy auth_service after fixing errors
```bash
# Rebuild the Docker image (from the auth directory)
cd /home/gokul/gokul_repos/go_microservice_project_1/system_design/pythonn/src/auth
docker build -t gokulkris/auth_service:latest .
docker push gokulkris/auth_service:latest

# Load it into minikube
minikube image load gokulkris/auth_service:latest

# Restart the pods to pick up the new image
kubectl rollout restart deployment auth
```

- to stop just the gateway services
```bash
kubectl scale deployment gateway --replicas=0
```

- `sudo vi /etc/hosts` to add the hostnames()

- `kubectl describe pod rabbitmq-0` to check the logs of the rabbitmq pod
- `kubectl describe pvc`

- `kubectl delete -f ./` to delete all the manifests