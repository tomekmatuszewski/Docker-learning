FROM ubuntu:latest

LABEL maintainer="tomasz_matuszewski@o2.pl"

RUN apt update && apt install nano -y
RUN apt install curl -y
ENV CURL_HOST https://onet.pl
CMD env
CMD curl -L $CURL_HOST && echo $EMAIL
