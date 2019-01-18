FROM tiangolo/uwsgi-nginx-flask:python3.6
MAINTAINER Andrew Clark - brassatc@icloud.com
# Set the working directory to /app
COPY ./app /app
RUN apt-get update
# install packages
RUN pip install -r requirements.txt
