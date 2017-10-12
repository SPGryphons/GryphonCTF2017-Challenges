FROM ubuntu:latest
ENV user=fileshare
RUN apt-get update
RUN apt-get install -y python3
RUN useradd -m $user
RUN mkdir -p /home/$user/flag
RUN mkdir -p /home/$user/files
COPY ./files/* /home/$user/files/
COPY ./flag/* /home/$user/flag/
COPY ./FS.py /home/$user/
RUN chown root:$user /home/$user/FS.py
RUN chmod 440 /home/$user/FS.py
RUN chown root:$user /home/$user/files
RUN chmod 660 /home/$user/files
RUN chmod +x /home/$user/files
RUN chown root:$user /home/$user/flag
RUN chmod 444 /home/$user/flag
RUN chmod +x /home/$user/flag
USER fileshare
WORKDIR /home/fileshare
EXPOSE 49760
CMD ["python3", "/home/fileshare/FS.py"]
