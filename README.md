# CS-612-Docker

This project is all about Docker initialization and RESTful web service.
flaskapp.py acts as rest service provider

Command to check images in repository of docker:
$docker image ls

Command To build image in docker container:
$docker build --tag=flask-app .

Command To run the flaskapp with web service using docker:
$docker run -p 4000:4200 flask-app

