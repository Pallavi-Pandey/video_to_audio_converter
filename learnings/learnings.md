# Microservice Architecture
- ![alt text](image.png)

- What is microservice Architecture?
    - is a type of architecture where the application is developed as a collection of services
    - Each service is a small, independent process that runs in its own process and communicates with other services through well-defined APIs.
    - Each service is responsible for a specific functionality and can be scaled independently.
    - Each service is developed and deployed independently.

- What is minikube?
    - minikube is a tool that allows you to run a single-node Kubernetes cluster on your local machine.
    - It is a great way to get started with Kubernetes and to test your applications in a local environment.
    - It is also a great way to learn about Kubernetes and to understand how it works.
    - It is a great way to test your applications in a local environment before deploying them to a production environment.
    - it is going to allow us to have a kubernetes cluster running on our local machine
   
- What is k9s?
    - k9s is a terminal-based UI for Kubernetes clusters.
    - It is a great way to get started with Kubernetes and to test your applications in a local environment.
    - It is also a great way to learn about Kubernetes and to understand how it works.
    - It is a great way to test your applications in a local environment before deploying them to a production environment.
    - it is going to allow us to have a kubernetes cluster running on our local machine
   
- in mysql
    - `show databases;`
        - this will show all the databases in the mysql server
    - `use auth;`
        - this will select the auth database
    - `show tables;`
        - this will show all the tables in the selected database
    - ` sudo mysql < init.sql `
        - this will run the sql file

    - `sudo mysql -e "DROP DATABASE auth;"`
        - this will drop the auth database
    - `sudo mysql -e "DROP USER auth_user@localhost;"`
        - this will drop the auth user
    - `show tables;`
        - this will show all the tables in the selected database
    - `describe user;s`
        - this will show the structure of the table

- Symmetic and Asymmetric signing algorithms
    - ![alt text](image-1.png)

- diff between datetime.datetime.now() and datetime.datetime.utcnow()
    - `datetime.datetime.now()` returns the current date and time in the local timezone
    - `datetime.datetime.utcnow()` returns the current date and time in UTC timezone

- diff between datetime.datetime.now(tz=datetime.timezone.utc) and datetime.datetime.utcnow()
    - `datetime.datetime.now(tz=datetime.timezone.utc)` returns the current date and time in UTC timezone
    - `datetime.datetime.utcnow()` returns the current date and time in UTC timezone
    - means both are same

- ![alt text](image-2.png)

- how do you optimize the docker image?
    - use multi stage build
    - use alpine as base image, because it is light weight and has less dependencies
    - alphine here means alpine linux, it is a light weight linux distribution
- alphine diff slim-bullseye
    
    
    

- pip freeze vs pip3 freeze?
    - the difference is that pip is the default python package manager and pip3 is the python 3 package manager

- how would you tag a docker image?
    - `docker tag <image_name> <tag>`

- stateful set
    - it is a type of deployment where the pods are assigned a unique identity
    - the pods are assigned a unique identity based on the order in which they are created
    - if a pod fails , the existing pod will not be deleted and a new pod will be created and the volume will be mounted to the new pod with the existing data
    - this is important for stateful applications like databases
    
- ![alt text](image-3.png)

- how are we going to persist data in rabbitmq
    - we can use a persistent volume to persist data in rabbitmq
![alt text](image-4.png)
- compare the gateway and rabbitmq containers in spec

- what is PVC(persistent volume claim)?
    - it is a request for a persistent volume
    - it is bound to a persistent volume, we will set how much storage we need in the pvc, it will interact with the persistent volume and bind it to the pvc
    - this means when a pod dies , the rabbitmq data will not be lost, it will be persisted in the persistent volume