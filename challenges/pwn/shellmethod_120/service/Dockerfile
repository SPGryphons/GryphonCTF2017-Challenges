FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" shellmethod

# Add xinetd configuration
ADD shellmethod.conf /etc/xinetd.conf

# Add challenge binary
ADD shellmethod-server-* /home/shellmethod/shellmethod

# Add flag to home
ADD flag.txt /home/shellmethod/flag.txt

# Change home
ENV HOME /home/shellmethod

# Double-enforce permissions
RUN chown -R root:root /home/shellmethod && \
    chown root:shellmethod /home/shellmethod/shellmethod && \
    chmod 2755 /home/shellmethod/shellmethod && \
    chown root:shellmethod /home/shellmethod/flag.txt && \
    chmod 0440 /home/shellmethod/flag.txt
