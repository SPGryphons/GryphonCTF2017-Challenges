#!/bin/sh

docker build -t lonelyplanet .
docker run -d -p 9119:59949 --name lonelyplanet lonelyplanet
