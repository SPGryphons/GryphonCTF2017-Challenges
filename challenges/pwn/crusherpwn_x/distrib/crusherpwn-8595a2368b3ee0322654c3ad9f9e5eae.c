/**
 * Created for GryphonCTF 2017_CrusherPwn
 * By Amos (LFlare) Ng <amosng1@gmail.com>
**/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int win() {
    system("/bin/cat flag.txt");
    return 0;
}

int main(int argc){
    // Create buffer
    char buf[128] = {0x00};

    // Get input
    fgets(buf, sizeof(buf), stdin);

    // Cry about input
    puts("=(");
    printf(buf);

    // Quit life
    exit(1);
}
