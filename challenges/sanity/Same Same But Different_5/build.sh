#!/bin/sh

docker build -t samesame .
sudo docker run -dt -p 17123:80 --name samesame samesame
docker start samesame