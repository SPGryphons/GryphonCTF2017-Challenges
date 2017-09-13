NAME = pseudoshell
CC = gcc
CFLAGS = -fno-stack-protector -mpreferred-stack-boundary=2 -Wno-implicit-function-declaration -m32

all:
	$(CC) ${NAME}.c $(CFLAGS) -o ../service/${NAME}-server
	$(CC) ${NAME}.c $(CFLAGS) -D REDACTED -o ../distrib/${NAME}-redacted
	cp $(NAME).c ../distrib/$(NAME).c

clean:
	rm ../service/${NAME}-server
	rm ../distrib/${NAME}-redacted
