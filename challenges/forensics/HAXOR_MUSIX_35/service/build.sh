#!/bin/sh

docker build -t haxor .
docker run -it -d -p 17651:80 --restart always --memory 64M --name foren-haxor haxor
docker start foren-haxor


