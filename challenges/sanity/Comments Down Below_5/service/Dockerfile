FROM httpd:2.4-alpine
RUN rm -rf /usr/local/apache2/htdocs/ && mkdir -p /usr/local/apache2/htdocs/
COPY ./index.html /usr/local/apache2/htdocs/
COPY ./.htaccess /usr/local/apache2/htdocs/
