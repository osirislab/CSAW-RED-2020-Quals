#include <stdio.h>
#include <stdlib.h>

#define FLAGBUF 40
#define INPUTBUF 32
#define OOPS 72

void all_I_do_is_win(int no, int matter, int what) {

	char buf[FLAGBUF];

	FILE *f = fopen("flag.txt","r");
	if (f == NULL) {
		printf("If you're seeing this, the flag file is missing. Please let an admin know!\n");
		exit(0);
	}

	fgets(buf,FLAGBUF,f);

	if (no != 0x600DC0DE){
    printf("Not quite.\n");
    return;
	}

	if (matter != 0xACCE5515){
    printf("You're getting there...\n");
    return;
	}

    if (what != 0xFEA51B1E){
    printf("So close!\n");
    return;
	}

	puts(buf);
	exit(0);
}

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
}

void vuln() {
	char buf[INPUTBUF];
	init();
	puts("Would you like to play a game? \nIf you can guess my three favorite numbers...you win!");
	fgets(buf, OOPS, stdin);
	return;
}

int main() {
	vuln();
	printf("Those numbers are the worst!\n");
	return 0;
}
