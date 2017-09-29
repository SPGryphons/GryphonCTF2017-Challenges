#!/bin/sh

docker build -t cookieagent .
docker run -it -d -p 17561:8080 --name cookieagent cookieagent 
docker start cookieagent
