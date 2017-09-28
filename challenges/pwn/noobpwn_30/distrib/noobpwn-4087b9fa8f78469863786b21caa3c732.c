/**
 * Created for the GryphonCTF 2017 challenges
 * By Amos (LFlare) Ng <amosng1@gmail.com>
**/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[], char* envp[]){
    // Create buffer
    char buf[32];

    // Check argument length
    if (argc < 2) {
        printf("Not enough arguments!\n");
        return 0;
    }

    // Create file descriptor
    int fd = atoi(argv[1]) - 0x1234;
    int len = read(fd, buf, 32);

    // Check if we have a winner
    if (!strcmp("GIMMEDAFLAG\n", buf)) {
        system("/bin/cat flag");
        exit(0);
    }

    // Return sadface
    return 1;
}
