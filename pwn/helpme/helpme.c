#include <stdio.h>

#define FLAGBUF = 40
#define INPUTBUF = 32

void binsh() {
	system("/bin/sh");
}

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
}

int main() {
	char buf[INPUTBUF];
	init();
	puts("I can never remember the command to open flag files... Can you do it for me? \n> ");
	gets(buf);
	printf("Hmm... Why didn't that work?\n");
	return 0;
}