#!/bin/sh
## [ security@dismgryphons.com ]
## Removed memory limit. Java uses more than 64MB which results in the process getting killed.
docker build -t cookieagent .
docker run --restart always -d -p 17561:8080 --name web-cookieagent cookieagent
docker start web-cookieagent
