FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" genesis

# Add xinetd configuration
ADD genesis.conf /etc/xinetd.conf

# Add challenge binary
ADD genesis-server-* /home/genesis/genesis

# Change home
ENV HOME /home/genesis

# Double-enforce permissions
RUN chown -R root:root /home/genesis && \
    chown root:genesis /home/genesis/genesis && \
    chmod 2755 /home/genesis/genesis
