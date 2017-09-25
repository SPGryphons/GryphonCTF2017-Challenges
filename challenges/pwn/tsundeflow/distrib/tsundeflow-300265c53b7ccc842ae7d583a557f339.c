/**
 * Created for the GryphonCTF 2017 challenges
 * By Amos (LFlare) Ng <amosng1@gmail.com>
**/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Check if built for redacted distrib
#ifdef REDACTED
    #define FLAG "GCTF{TSUNDEFLOW_FLAG}"
#else
    #define FLAG "GCTF{51mpl3_buff3r_0v3rfl0w_f0r_75und3r35}"
#endif

int win() {
    puts("B-baka! It's not like I like you or anything!");
    puts(FLAG);
}

int main() {
    // Disable output buffering
    setbuf(stdout, NULL);

    // Declare main variables
    char input[32];

    // User preface
    puts("I check input length now! Your attacks have no effect on me anymore!!!");
    printf("Your response? ");

    // Read user input
    scanf("%s", input);

    // "Check" for buffer overflow
    if (strlen(input) > 32) {
        exit(1);
    }
}
