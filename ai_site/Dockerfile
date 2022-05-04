# ai-site/Dockerfile

# pull the official docker image
FROM python:3.8

# set work directory
WORKDIR /ai_site

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY . /ai_site
RUN pip install -r requirements.txt