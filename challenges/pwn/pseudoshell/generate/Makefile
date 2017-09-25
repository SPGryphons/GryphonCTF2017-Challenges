NAME = pseudoshell
CC = gcc
CFLAGS = -fno-stack-protector -mpreferred-stack-boundary=2 -Wno-implicit-function-declaration -m32

all:
	$(CC) ${NAME}.c $(CFLAGS) -o ../service/${NAME}-server
	$(CC) ${NAME}.c $(CFLAGS) -D REDACTED -o ../distrib/${NAME}-redacted
	cp $(NAME).c ../distrib/$(NAME).c
	mv ../service/${NAME}-server ../service/${NAME}-server-`md5sum ../service/${NAME}-server | cut -b-32`
	mv ../distrib/${NAME}-redacted ../distrib/${NAME}-redacted-`md5sum ../distrib/${NAME}-redacted | cut -b-32`
	mv ../distrib/${NAME}.c ../distrib/${NAME}-`md5sum ../distrib/${NAME}.c | cut -b-32`.c

clean:
	rm ../service/${NAME}*
	rm ../distrib/${NAME}*
