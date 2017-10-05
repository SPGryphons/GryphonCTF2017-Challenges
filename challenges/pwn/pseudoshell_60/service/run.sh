#! /bin/bash
##
# Created for GryphonCTF 2017_PseudoShell
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Get port number to bind to
PORT=${PORT:-"17341"}

# Run container
docker rm -f pseudoshell
docker run \
    --name pseudoshell \
    --detach \
    --tty \
    --publish ${PORT}:9999 \
    --restart always \
    --memory 64M \
    pseudoshell
