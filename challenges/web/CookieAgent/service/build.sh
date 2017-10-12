#!/bin/sh
## [ security@dismgryphons.com ]
docker build -t cookieagent .
docker run --restart always -d -p 17561:8080 --name web-cookieagent cookieagent
docker start web-cookieagent
