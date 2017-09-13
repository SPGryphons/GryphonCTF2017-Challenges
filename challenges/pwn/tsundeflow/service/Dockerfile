FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" tsundeflow

# Switch to user
USER tsundeflow

# Add xinetd configuration
ADD tsundeflow.conf /etc/xinetd.conf

# Add challenge binary
ADD tsundeflow-server /home/tsundeflow/tsundeflow
