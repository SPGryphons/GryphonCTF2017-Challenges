FROM tomcat:8.0-jre8-alpine
COPY ./server.xml /usr/local/tomcat/conf/
COPY ./web.xml /usr/local/tomcat/conf/
RUN chmod -R 400 /usr/local/tomcat/conf/
RUN mkdir -p /usr/local/tomcat/lib/org/apache/catalina/util
COPY ./ServerInfo.properties /usr/local/tomcat/lib/org/apache/catalina/util/ServerInfo.properties
RUN rm -rf /usr/local/tomcat/webapps/ && mkdir -p /usr/local/tomcat/webapps/
COPY ./CookieAgent.war /usr/local/tomcat/webapps/ROOT.war
