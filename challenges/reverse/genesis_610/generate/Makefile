NAME = genesis
CC = gcc
CFLAGS = -lm -pthread -fstack-protector-all -m32
TROLL = irc.c

all:
	$(CC) ${NAME}.c $(CFLAGS) -o ../service/${NAME}-server
	$(CC) ${NAME}.c $(CFLAGS) -D REDACTED -include ${TROLL} -o ../distrib/${NAME}-redacted
	mv ../service/${NAME}-server ../service/${NAME}-server-`md5sum ../service/${NAME}-server | cut -b-32`
	mv ../distrib/${NAME}-redacted ../distrib/${NAME}-redacted-`md5sum ../distrib/${NAME}-redacted | cut -b-32`

clean:
	rm ../service/${NAME}-*
	rm ../distrib/${NAME}*
