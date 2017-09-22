#!/bin/sh
docker build -t fileshare .
docker run -dt -p 17425:49760  --name fileshare fileshare
