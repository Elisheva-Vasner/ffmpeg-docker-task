FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \ 
apt-get install -y ffmpeg && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

WORKDIR /my_first_processing

ENTRYPOINT ["ffmpeg"]

