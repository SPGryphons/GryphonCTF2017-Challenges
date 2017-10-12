#!/bin/sh
docker build -t bashing .
docker run --restart always --memory 128M -dt -p 17345:25000 --name pwn-bashing bashing
docker start pwn-bashing
