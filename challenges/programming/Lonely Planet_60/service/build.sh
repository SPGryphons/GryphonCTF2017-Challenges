#!/bin/sh

docker build -t lonelyplanet .
docker run -d -p 17417:59949 --name lonelyplanet lonelyplanet
