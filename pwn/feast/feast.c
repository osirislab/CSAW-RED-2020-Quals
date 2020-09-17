#include <stdio.h>

#define FLAGBUF = 40
#define INPUTBUF = 32

void winner_winner_chicken_dinner() {
	char buf[FLAGBUF];
	FILE *f = fopen("flag.txt","r");
	if (f == NULL) {
		printf("If you receive this output, the flag file is missing. Please let an admin know!\n");
		exit(0);
	}

	fgets(buf,FLAGBUF,f);
	printf(buf);
	exit(0);
}

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
}

int main() {
	char buf[INPUTBUF];
	init();
	puts("Welcome to the feast! \nThere's a delicious dinner waiting for you, if you can get to it!\n > ");
	gets(buf); //ruh-roh
	printf("Oh, not hungry? Maybe next time.");
	return 0;
}