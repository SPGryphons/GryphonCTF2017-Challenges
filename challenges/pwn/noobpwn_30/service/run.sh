#! /bin/bash
##
# Created for GryphonCTF 2017 Tsundeflow
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Get port number to bind to
PORT=${PORT:-"17335"}

# Run container
docker rm -f noobpwn
docker run \
    --name noobpwn \
    --detach \
    --tty \
    --publish ${PORT}:9999 \
    --restart always \
    --memory 64M \
    noobpwn
