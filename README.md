# Dockerized Ai site 

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This is Dockerized version of backend part of AI site.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be
```
cd ai_site
```
```
docker-compose up -d --build   
```
```
docker-compose exec web python manage.py migrate --noinput
```
Open in your browser
```
localhost
```

## Usage <a name = "usage"></a>

Add notes about how to use the system:
* Django
* Docker
* Postgres

### NGINX
if you want change name from "localhost" to another you should change config in nginx dir
