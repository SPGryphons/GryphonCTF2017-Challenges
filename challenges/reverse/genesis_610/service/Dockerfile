FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" genesis

# Switch to user
USER genesis

# Add xinetd configuration
ADD genesis.conf /etc/xinetd.conf

# Add challenge binary
ADD genesis-server-* /home/genesis/genesis
