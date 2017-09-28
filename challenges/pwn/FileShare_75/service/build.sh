#!/bin/sh
docker build -t fileshare .
docker run -dt -p 17342:49760  --name fileshare fileshare
