#!/bin/sh
docker build -t lonelyplanet .
docker run --restart always --memory 64M -d -p 17453:59949 --name prog-lonelyplanet lonelyplanet
docker start prog-lonelyplanet
