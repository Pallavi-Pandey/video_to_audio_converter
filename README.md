# go_microservice_project_1

- we are developing a video to audio converter application using python,mogodb,mysql,kubernetes,rabbitmq


Flow
    - when a user upload a video to be converted to mp3, that request will first hit our gateway, then our gateway will store the video in mongodb and send a message to rabbitmq(queue) letting downstream services know that there is a new video to be converted to mp3 in mongodb
    - the video to mp3 converted service will consume messages from the queue
    - it will take the id of the video from the message, pull it from the mongo db, convert it to mp3 and store it in mongodb
    - then put a new message on the queue to be consumed by the notification service that says the conversion job is done
    - the notification service will consume the message and send an email notification to the client , 
    - the client will use the notification_id and his jwt to request the gateway to return the converted mp3 file
    - api gateway will pull the file from mongodb and return it to the client

- 