#!/bin/sh

docker build -t comments .
sudo docker run -dt -p 17121:80 --name comments comments
docker start comments