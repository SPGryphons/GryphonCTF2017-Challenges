#!/bin/sh

docker build -t san-comments .
docker run -it -d -p 17121:80 --restart always --memory 64M --name san-comments comments 
docker start san-comments