#!/bin/sh

docker build -t samesame .
docker run -it -d -p 17123:80 --restart always --memory 64M --name san-samesame samesame 
docker start san-samesame