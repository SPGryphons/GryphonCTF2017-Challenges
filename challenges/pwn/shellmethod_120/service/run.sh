#! /bin/bash
##
# Created for GryphonCTF 2017 Tsundeflow
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Get port number to bind to
PORT=${PORT:-"17344"}

# Run container
docker rm -f pwn-shellmethod
docker run \
    --name pwn-shellmethod \
    --detach \
    --tty \
    --publish ${PORT}:9999 \
    --restart always \
    --memory 64M \
    shellmethod
