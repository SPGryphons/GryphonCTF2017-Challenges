FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" crusherpwn

# Add xinetd configuration
ADD crusherpwn.conf /etc/xinetd.conf

# Add entrypoint
ADD entrypoint.sh /bin/entrypoint

# Add challenge binary
ADD crusherpwn-server-* /home/crusherpwn/crusherpwn

# Add flag to home
ADD flag.txt /home/crusherpwn/flag.txt

# Change home
ENV HOME /home/crusherpwn

# Double-enforce permissions
RUN chown -R root:root /home/crusherpwn && \
    chown root:crusherpwn /home/crusherpwn/crusherpwn && \
    chmod 2755 /home/crusherpwn/crusherpwn && \
    chown root:crusherpwn /home/crusherpwn/flag.txt && \
    chmod 0440 /home/crusherpwn/flag.txt
