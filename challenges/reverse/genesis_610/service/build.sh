#!/bin/sh
## [ security@dismgryphons.com ]
## Simplified build script
docker build -t genesis .
docker run --restart always --memory 64M -dt -p 17234:9999 --name rev-genesis genesis
docker start rev-genesis
