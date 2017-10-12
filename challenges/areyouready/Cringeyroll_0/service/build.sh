#!/bin/sh
docker build -t cringeyroll .
docker run --restart always --memory 64M -d -p 17122:80 --name san-cringeyroll cringeyroll
docker start san-cringeyroll
