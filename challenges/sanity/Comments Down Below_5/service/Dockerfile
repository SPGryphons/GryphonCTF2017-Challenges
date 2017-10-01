FROM debian:sid
RUN apt-get update
RUN apt-get install -y apache2
COPY ./index.html /var/www/html/.
EXPOSE 80
RUN service apache2 start
CMD apachectl -D FOREGROUND