FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" tsundeflow

# Add xinetd configuration
ADD tsundeflow.conf /etc/xinetd.conf

# Add challenge binary
ADD tsundeflow-server-* /home/tsundeflow/tsundeflow

# Add flag to home
ADD flag.txt /home/tsundeflow/flag.txt

# Double-enforce permissions
RUN chown -R root:root /home/tsundeflow && \
    chown root:tsundeflow /home/tsundeflow/tsundeflow && \
    chmod 2755 /home/tsundeflow/tsundeflow && \
    chown root:tsundeflow /home/tsundeflow/flag.txt && \
    chmod 0440 /home/tsundeflow/flag.txt
