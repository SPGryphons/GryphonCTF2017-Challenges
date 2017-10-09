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
    int key = 0x00;
    char buf[128] = {0x00};
    char confirm = 0x00;

    // Disable output buffering
    setbuf(stdout, NULL);

    // Get player's name
    puts("Hello, welcome to the playground!");
    puts("What's your name?");
    fgets(buf, sizeof(buf), stdin);

    // Confirm player's name
    printf("Can you confirm that your name is indeed, ");
    printf(buf);
    printf("Please enter [Y/N] to confirm: ");
    confirm = getchar();

    // Check confirmation
    if (confirm == 'Y') {
        // Check if we are authorized
        if (key == 0x1337) {
            puts("Successfully authorized!");
            win();
        } else {
            puts("You are not authorized!");
            exit(1);
        }
    }
}
