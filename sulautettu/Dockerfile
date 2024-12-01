FROM debian:bookworm

WORKDIR /app

COPY ./material .

RUN apt-get update

RUN apt-get install -y file binwalk default-jdk unzip
