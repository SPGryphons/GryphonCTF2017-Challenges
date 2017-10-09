#! /bin/bash
##
# Created for GryphonCTF 2017_CrusherPwn
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Get port number to bind to
PORT=${PORT:-"17346"}

# Run container
docker rm -f crusherpwn
docker run \
    --name crusherpwn \
    --detach \
    --tty \
    --publish ${PORT}:9999 \
    --restart always \
    --memory 64M \
    crusherpwn
