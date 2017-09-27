FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" pseudoshell

# Switch to user
USER pseudoshell

# Add xinetd configuration
ADD pseudoshell.conf /etc/xinetd.conf

# Add challenge binary
ADD pseudoshell-server-* /home/pseudoshell/pseudoshell

# Add flag to home
ADD flag.txt /home/pseudoshell/flag.txt
