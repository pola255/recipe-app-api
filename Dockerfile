# 3.7-alpine is the image name find it on docker Hub
FROM python:3.7-alpine
# The MAINTAINER line is optional and show who maintain the project.
# Company name that is fine
MAINTAINER London App Developer Ltd.
# python an buffer environment variable;
# It says python that executes in no buffer mode, 
# it is recommendable when running python in docker containers
ENV PYTHONUNBUFFERED 1

# Install dependencies in requirenment.txt
# copy our requirenment.txt to the docker image requirenment.txt
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
# run requirenment.txt using pip
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
# create empty folder in our docker image
RUN mkdir /app
# Indicate to start thye app in this location
WORKDIR /app
# then copy the app of my local machine to the docker app folder
COPY ./app/ /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
# create the user that will execute our app using docker
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
# switch to the User we created
USER user
