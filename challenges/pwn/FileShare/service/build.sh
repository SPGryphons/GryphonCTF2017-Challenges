#!/bin/sh
docker build -t fileshare .
docker run --restart always --memory 128M -dt -p 17342:49760 --name pwn-fileshare fileshare
docker start pwn-fileshare
