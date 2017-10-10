#!/bin/sh
docker build -t lecturersays .
docker run --restart always --memory 64M -d -p 17451:9999 --name prog-lecturersays lecturersays
docker start prog-lecturersays
