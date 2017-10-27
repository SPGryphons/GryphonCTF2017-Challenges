FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" pseudoshell

# Add xinetd configuration
ADD pseudoshell.conf /etc/xinetd.conf

# Add entrypoint
ADD entrypoint.sh /bin/entrypoint

# Add challenge binary
ADD pseudoshell-server-* /home/pseudoshell/pseudoshell

# Add flag to home
ADD flag.txt /home/pseudoshell/flag.txt

# Change home
ENV HOME /home/pseudoshell

# Double-enforce permissions
RUN chown -R root:root /home/pseudoshell && \
    chown root:pseudoshell /home/pseudoshell/pseudoshell && \
    chmod 2755 /home/pseudoshell/pseudoshell && \
    chown root:pseudoshell /home/pseudoshell/flag.txt && \
    chmod 0440 /home/pseudoshell/flag.txt
