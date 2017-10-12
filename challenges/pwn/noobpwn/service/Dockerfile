FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" noobpwn

# Add xinetd configuration
ADD noobpwn.conf /etc/xinetd.conf

# Add entrypoint
ADD entrypoint.sh /bin/entrypoint

# Add challenge binary
ADD noobpwn-server-* /home/noobpwn/noobpwn

# Add flag to home
ADD flag.txt /home/noobpwn/flag.txt

# Change home
ENV HOME /home/noobpwn

# Double-enforce permissions
RUN chown -R root:root /home/noobpwn && \
    chown root:noobpwn /home/noobpwn/noobpwn && \
    chmod 2755 /home/noobpwn/noobpwn && \
    chown root:noobpwn /home/noobpwn/flag.txt && \
    chmod 0440 /home/noobpwn/flag.txt
