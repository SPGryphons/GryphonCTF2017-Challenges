NAME = genesis
CC = gcc
CFLAGS = -lm -pthread -fstack-protector-all -m32
TROLL = irc.c

all:
	$(CC) ${NAME}.c $(CFLAGS) -o ../service/${NAME}-server
	$(CC) ${NAME}.c $(CFLAGS) -D REDACTED -include ${TROLL} -o ../distrib/${NAME}-redacted

clean:
	rm ../service/${NAME}-server
	rm ../distrib/${NAME}-redacted
