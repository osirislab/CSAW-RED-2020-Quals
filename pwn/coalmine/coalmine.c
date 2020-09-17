#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define FLAGBUF 40
#define INPUTBUF 32
#define BIRDBUF 8

char global_birdy[BIRDBUF];

void tweet_tweet() {
	char buf[FLAGBUF];
	FILE *f = fopen("flag.txt","r");
	if (f == NULL) {
		printf("If you receive this output, the flag file is missing. Please let an admin know!\n");
		exit(0);
	}

	fgets(buf,FLAGBUF,f);
	puts(buf);
	exit(0);
}

void carry_bird_into_mine() {
	FILE *f = fopen("birdy.txt","r");
	if (f == NULL) {
		printf("Necessary challenge file missing. Please let an admin know!\n");
		exit(0);
	}
	fread(global_birdy,1,BIRDBUF,f);
	fclose(f);
}

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
}

int main() {
	char birdy[BIRDBUF];
	char buf[INPUTBUF];
	init();
  carry_bird_into_mine();
	memcpy(birdy,global_birdy,BIRDBUF);
	printf("Working in a coal mine is dangerous stuff. \nGood thing I've got my bird to protect me. \nCan you hear it singing? \n> ");
	gets(buf);

	if (memcmp(birdy,global_birdy,BIRDBUF)) {
      printf("*** Dangerous Stack Activity Detected *** : What did you do to my Canary?!\n");
      exit(-1);
   }

	if (buf == "yes") {
		puts("Phew. Better get back to work then.");
	}
	else if (buf == "no") {
		puts("Uh-oh! I've got to get out of here!");
	}
	else {
		puts("Listen closer...");
	}
	return 0;
}
