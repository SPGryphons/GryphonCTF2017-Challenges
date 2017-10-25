FROM lflare/xinetd:latest
MAINTAINER Amos (LFlare) Ng <amosng1@gmail.com>

# Create user
RUN adduser --disabled-password --gecos "" speedfart

# Add xinetd configuration
ADD speedfart.conf /etc/xinetd.conf

# Add challenge script
ADD speedfart.py /home/speedfart/speedfart

# Change home
ENV HOME /home/speedfart

# Double-enforce permissions
RUN chown -R root:root /home/speedfart && \
    chown root:speedfart /home/speedfart/speedfart && \
    chmod 2755 /home/speedfart/speedfart
