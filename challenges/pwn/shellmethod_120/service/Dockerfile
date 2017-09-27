FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" shellmethod

# Switch to user
USER shellmethod

# Add xinetd configuration
ADD shellmethod.conf /etc/xinetd.conf

# Add challenge binary
ADD shellmethod-server-* /home/shellmethod/shellmethod

# Add flag to home
ADD flag.txt /home/shellmethod/flag.txt
