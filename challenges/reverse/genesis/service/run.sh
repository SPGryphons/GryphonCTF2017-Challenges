#! /bin/bash
##
# Created for GryphonCTF 2017 Genesis
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Get port number to bind to
PORT=${PORT:-"17334"}

# Run container
docker rm -f genesis
docker run \
    --name genesis \
    --detach \
    --tty \
    --publish ${PORT}:9999 \
    --restart always \
    --memory 64M \
    genesis
