#!/bin/sh
docker build -t comments .
docker run --restart always --memory 64M -d -p 17121:80 --name san-comments comments
docker start san-comments
