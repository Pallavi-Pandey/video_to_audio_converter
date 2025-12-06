
1) youtube link
- https://youtu.be/hmkF77F9TLw

2) original repo link - https://github.com/kantancoding/microservices-python

3) install kubectl 
- https://kubernetes.io/docs/tasks/tools/
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check 
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
chmod +x kubectl
mkdir -p ~/.local/bin
mv ./kubectl ~/.local/bin/kubectl
kubectl version --client
```


4) install minikube
https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download

```
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

5) install k9s
https://github.com/derailed/k9s

```
wget https://github.com/derailed/k9s/releases/latest/download/k9s_linux_amd64.deb \
&& sudo apt install ./k9s_linux_amd64.deb -y \
&& rm k9s_linux_amd64.deb
```
