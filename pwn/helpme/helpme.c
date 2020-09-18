#include <stdio.h>
#include <stdlib.h>

#define INPUTBUF 32

void binsh() {
	system("/bin/sh");
}

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
}

void vuln() {
	char buf[INPUTBUF];
	printf("I can never remember the command to open flag files... \nCan you do it for me? \n> ");
	gets(buf);
}

int main() {
	init();
	vuln();
	printf("Hmm... Well that didn't work...\n");
	return 0;
}
