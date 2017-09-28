FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" noobpwn

# Switch to user
USER noobpwn

# Add xinetd configuration
ADD noobpwn.conf /etc/xinetd.conf

# Add challenge binary
ADD noobpwn-server-* /home/noobpwn/noobpwn

# Add flag to home
ADD flag.txt /home/noobpwn/flag.txt
