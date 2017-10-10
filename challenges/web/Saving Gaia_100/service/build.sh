#!/bin/sh
docker build -t gaia .
docker run --restart always --memory 128M -d -p 17565:80 --name web-gaia gaia
docker start web-gaia
