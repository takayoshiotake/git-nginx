FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y \
  fcgiwrap \
  git \
  nginx
RUN apt-get install -y \
  python3 \
  python3-pip \
  python3-venv
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /opt/git

COPY auth/ /opt/auth/
RUN bash /opt/auth/build.sh

COPY start.sh start.dev.sh /root/
CMD bash /root/start.sh
