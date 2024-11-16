FROM debian:bookworm

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install -y make gcc micro

RUN make crackme01e

RUN make crackme02

RUN make crackme02e