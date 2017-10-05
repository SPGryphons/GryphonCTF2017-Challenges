#! /bin/bash
##
# Created for GryphonCTF 2017_Genesis
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Get port number to bind to
PORT=${PORT:-"17234"}

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
