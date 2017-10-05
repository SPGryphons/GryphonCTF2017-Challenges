/**
 * Created for the GryphonCTF 2017 challenges
 * By Amos (LFlare) Ng <amosng1@gmail.com>
**/
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <sys/ptrace.h>
#include <unistd.h>

// Check if built for redacted distrib
#ifdef REDACTED
    #define FLAG_ONE "GCTF{FLAG_ONE}"
    #define FLAG_TWO "GCTF{FLAG_TWO}"
    #define FLAG_THREE "GCTF{FLAG_THREE}"
    #define FLAG_FOUR "GCTF{FLAG_FOUR}"
    #define FLAG_FIVE "GCTF{FLAG_FIVE}"
    #define FLAG_BONUS "GCTF{FLAG_BONUS}"
#else
    #define FLAG_ONE "GCTF{w3lc0m3_70_r3v3r53_3n61n33r1n6}"
    #define FLAG_TWO "GCTF{ch4r_p01n73r5_!=_ch4r_4rr4y}"
    #define FLAG_THREE "GCTF{r3v3r51n6_b175_4r3_c00l}"
    #define FLAG_FOUR "GCTF{b17_c0un71n6_w17h_b17_7w1ddl1n6}"
    #define FLAG_FIVE "GCTF{1nv3r53_r0075_m4d3_1n3ff1c13n7}"
    #define FLAG_BONUS "GCTF{1rc_15_p0pul4r_4m0n6_c7f_pl4y3r5_700}"
#endif

// Declare classic banner
char *banner = "================================================================\n"
               "                            LEVEL %02d                              \n"
               "================================================================\n"
               "Enter secret code: ";

int level_one() {
    // Declare level variables
    char *challenge = "7h15 15 4 h1dd3n 57r1n6";
    char input[32];

    // Print challenge
    printf(banner, 1);

    // Read input
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;

    // Compare string
    if (strcmp(challenge, input) == 0) {
        return 1;
    }
    return 0;
}

int level_two() {
    // Declare level variables
    char challenge[] = "7h1nk1n6 w17h 1n7363r5!1";
    char input[32];

    // Print challenge
    printf(banner, 2);

    // Read input
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;

    // Compare string
    if (strcmp(challenge, input) == 0) {
        return 1;
    }
    return 0;
}

int tumbalek(char c) {
    // Basically reverses all the bits in the char
    c = (c & 0xF0) >> 4 | (c & 0x0F) << 4;
    c = (c & 0xCC) >> 2 | (c & 0x33) << 2;
    c = (c & 0xAA) >> 1 | (c & 0x55) << 1;
    return c;
}

int level_three() {
    // Declare level variables
    // char challenge[] = "r3v3r53 3n61n33r5";
    int challenge[] = {0x4E, 0xFFFFFFCC, 0x6E, 0xFFFFFFCC, 0x4E, 0xFFFFFFAC, 0xFFFFFFCC, 0x04, 0xFFFFFFCC, 0x76, 0x6C, 0xFFFFFF8C, 0x76, 0xFFFFFFCC, 0xFFFFFFCC, 0x4E, 0xFFFFFFAC};
    int length = sizeof(challenge)/sizeof(challenge[0]);
    char input[32];

    // Print challenge
    printf(banner, 3);

    // Read input
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;

    for (int i = 0; i < length; i++) {
        if (input[i] != tumbalek(challenge[i])) {
            return 0;
        }
    }

    return 1;
}

int ordinal(int input) {
    int one_bits = 0;

    while (input > 0) {
        one_bits += input & 0x1;
        input >>= 1;
    }

    return one_bits;
}

int level_four() {
    // Declare level variables
    char challenge[] = "GCTF_TOO_FUN";
    int attempt[12];

    // Ensure unusability of GDB
    #ifdef REDACTED
    if (ptrace(PTRACE_TRACEME, 0, NULL, 0) == -1) {
        printf("GDB IS NOT ALLOWED!\n");
        return 1;
    }
    #endif

    // Print challenge
    printf(banner, 4);

    // Read input
    scanf("%d %d %d %d %d %d %d %d %d %d %d %d", &attempt[0], &attempt[1], &attempt[2], &attempt[3], &attempt[4], &attempt[5], &attempt[6], &attempt[7], &attempt[8], &attempt[9], &attempt[10], &attempt[11]);
    while (getchar() != '\n');

    for (int i = 0; i < strlen(challenge); i++) {
        if (ordinal(challenge[i]) != attempt[i]) {
            return 0;
        }
    }
    return 1;
}

float fov(float z) {
    long a, e, f, h;
    float b, c, g;
    const float d = 1.5F;

    e  = z * d;
    f  = 0x8504f35f - (e << 3);
    b  = z * 0.5F;
    c  = z;
    g  = f << 2;
    a  = *(long *) &c;
    f  = a;
    a  = c * c * b;
    a  = 0x5f3759df - (f >> 1);
    c  = *(float *) &a;
    h  = z + d;
    c  = c * (d - (b * c * c));

    return c;
}

// Quake
int level_five() {
    // Declare level variables
    int challenge[] = {3, 1, 3, 3, 7};
    float attempt[5];

    // Print challenge
    printf(banner, 5);

    // Read input
    scanf("%f %f %f %f %f", &attempt[0], &attempt[1], &attempt[2], &attempt[3], &attempt[4]);
    while (getchar() != '\n');

    for (int i = 0; i < 5; i++) {
        printf("%d %d\n", (int)round(fov(attempt[i])), challenge[i]);
        if ((int)round(fov(attempt[i])) != challenge[i]) {
            return 0;
        }
    }
    return 1;
}

int bonus() {
    // Declare level variables
    #ifdef REDACTED
    char challenge[] = "d1d y0u 7h1nk 7h15 w0uld b3 345y?";
    #else
    char challenge[] = "1n73rn37 r34lly ch4rm5";
    #endif
    char input[32];

    // Print challenge
    printf(banner, 99);

    // Read input
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;

    // Compare string
    if (strcmp(challenge, input) == 0) {
        return 1;
    }
    return 0;
}

int main() {
    // Disable output buffering
    setbuf(stdout, NULL);

    // Start the challenge of doom
    if (level_one()) {
        puts(FLAG_ONE);

        if (level_two()) {
            puts(FLAG_TWO);

            if (level_three()) {
                puts(FLAG_THREE);

                if (level_four()) {
                    puts(FLAG_FOUR);

                    if (level_five()) {
                        puts(FLAG_FIVE);

                        if (bonus()) {
                            puts(FLAG_BONUS);
                        }
                    }
                }
            }
        }
    }

    // Print noob message
    puts("y0u 4r3n'7 600d 3n0u6h!");
    return 1;
}
