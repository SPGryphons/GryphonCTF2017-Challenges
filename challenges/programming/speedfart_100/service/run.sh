#! /bin/bash
##
# Created for GryphonCTF 2017_SpeedFart
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Get port number to bind to
PORT=${PORT:-"17455"}

# Run container
docker rm -f speedfart
docker run \
    --name speedfart \
    --detach \
    --tty \
    --publish ${PORT}:9999 \
    --restart always \
    --memory 64M \
    speedfart
