#!/bin/sh

docker build -t lonelyplanet .
docker run -d -p 17453:59949 --name lonelyplanet lonelyplanet
