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