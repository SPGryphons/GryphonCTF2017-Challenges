#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main() {
	srand(time(0));
	int r = rand()%1000000;
	printf("Here is a random number: %d\n", r);
	char * flag = "GCTF{i_th1nk_i_m4y_h4v3_f0rg077en_th15}";
}