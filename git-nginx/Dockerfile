FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y \
  fcgiwrap \
  git \
  nginx
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /opt/git

CMD /etc/init.d/fcgiwrap start && \
  /usr/sbin/nginx -g "daemon off;"
