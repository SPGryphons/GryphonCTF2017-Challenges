#!/bin/sh
docker build -t samesame .
docker run --restart always --memory 64M -d -p 17123:80 --name san-samesame samesame
docker start san-samesame
