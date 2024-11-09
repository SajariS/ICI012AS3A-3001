FROM debian:bookworm

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install -y make gcc micro

RUN make

CMD ["./passtr"]