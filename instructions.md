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

- to check logs of a container
    `kubectl logs -f converter-7996656bf8-kr2q2`
    - `kubectl describe pod converter-7996656bf8-kr2q2 | tail -30`
    - `kubectl logs converter-7996656bf8-hjwkl`
    - `kubectl get pods -l app=converter`

```bash
# Build the image
cd /home/gokul/gokul_repos/go_microservice_project_1/system_design/pythonn/src/converter
docker build -t gokulkris/converter:latest .

# Push to Docker Hub
docker push gokulkris/converter:latest

# Restart the deployment to pull the new image
kubectl rollout restart deployment converter
```

- `curl -X POST http://mp3converter.com/login -u gokul@gmail.com:gokul123`

```bash
# Stream logs from one pod (follow mode)
kubectl logs -f gateway-6d8c55d7cb-8smnv

# Or stream logs from ALL gateway pods at once
kubectl logs -f -l app=gateway

# Or just get recent logs (last 50 lines)
kubectl logs -l app=gateway --tail=50
```

- to scale the deployments to one replicas for easy debugging
```bash
kubectl scale deployment gateway --replicas=1
kubectl scale deployment auth --replicas=1
kubectl scale deployment converter --replicas=1
```

- to delete the gateway 
```bash
kubectl delete -f ./manifests
```

- `kubectl exec -it mongodb-5ff6db945b-v8pgw -- mongosh`
- `show databases`
- `use mp3s`
- `show collections`
- `db.fs.files.find()`

- `db.fs.files.find({"_id": ObjectId("6954f73eaaf3d46526cfe494")})`

```bash to download the audio from mongo in kube to local
kubectl exec mongodb-5ff6db945b-v8pgw -- mongofiles --db=mp3s get_id '{"$oid": "6954f73eaaf3d46526cfe494"}' --local=- > local_music_file.mp3
```

- to login to mysql in kube(check the password from mysql-secret.yaml)
- `kubectl exec -it auth-mysql-84688dbb58-6dq5m -- mysql -u root -p -h 127.0.0.1`

- `update user set email = "gokulakrishananm1998@gmail.com" where id=1;`


```bash
curl -X POST -F 'file=@/home/gokul/videoplayback.mp4' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imdva3VsYWtyaXNobmFubTE5OThAZ21haWwuY29tIiwiYXV0aHoiOnRydWUsImV4cCI6MTc2NzI3MjMwMywiaWF0IjoxNzY3MTg1OTAzfQ.RmnBtY7pP649BYAH3P8R-axSX4d2bv_B3WbvV6BJ9r4' http://mp3converter.com/upload
```

- `to delete a pod in k9 press ctrl+d and then press enter`  


```bash
kubectl scale deployment --replicas=1 gateway converter auth notification
```

```bash
kubectl create secret generic notification-secret --from-env-file=system_design/pythonn/src/notification/.env --dry-run=client -o yaml | kubectl apply -f -
kubectl rollout restart deployment/notification
```

- you can even sh into any of the pods
```bash
k9s
select the pod and press enter
then press  s
env| grep GMAIL
```


- to download the audio with curl
```bash
curl --output mp3_download.mp3 -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imdva3VsYWtyaXNobmFubTE5OThAZ21haWwuY29tIiwiYXV0aHoiOnRydWUsImV4cCI6MTc2NzI3MjMwMywiaWF0IjoxNzY3MTg1OTAzfQ.RmnBtY7pP649BYAH3P8R-axSX4d2bv_B3WbvV6BJ9r4" "http://mp3converter.com/download?fid=69553048ea13db3580da57d9"
```