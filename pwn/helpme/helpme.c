#include <stdio.h>
#include <stdlib.h>

#define INPUTBUF 32

void binsh() {
	system("/bin/sh");
}

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
}

int main() {
	char buf[INPUTBUF];
	init();
	printf("I can never remember the command to open flag files... \nCan you do it for me? \n> ");
	gets(buf);
	printf("Hmm... Well that didn't work...\n");
	return 0;
}
