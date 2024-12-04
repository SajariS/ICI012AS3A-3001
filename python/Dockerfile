FROM debian:bookworm

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install -y micro fzf exuberant-ctags python3 git

RUN micro --plugin install jump

RUN git clone https://github.com/terokarvinen/palettero.git 

RUN git clone https://github.com/terokarvinen/micro-run.git 

RUN git clone https://github.com/terokarvinen/micro-cheat.git 

RUN mv micro-run micro-cheat palettero $HOME/.config/micro/plug/