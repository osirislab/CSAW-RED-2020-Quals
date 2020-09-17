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
		puts("If you receive this output, then there's no flag.txt on the server -- message an admin on Discord.");
        puts("Alternatively, you may be testing your code locally, in which case you need a fake flag.txt file in your directory.");
		exit(0);
	}

	fgets(buf,FLAGBUF,f);
	puts(buf);
	exit(0);
}

void carry_bird_into_mine() {
	FILE *f = fopen("birdy.txt","r");
	if (f == NULL) {
		printf("Looks like the bird has left the server. -- Please let an admin know on Discord!\n");
		printf("If you're running this locally, you'll need a birdy of your own!");
		exit(0);
	}
	fread(global_birdy,1,BIRDBUF,f);
	fclose(f);
}

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
}

void name_it() { 
   char birdy[BIRDBUF];
   char input[INPUTBUF];
   char length[INPUTBUF];
   int count;
   int x = 0;
   memcpy(birdy,global_birdy,BIRDBUF);
   printf("How many letters should its name have?\n> ");
   while (x<INPUTBUF) {
      read(0,length+x,1);
      if (length[x]=='\n') break;
      x++;
   }

   sscanf(length,"%d",&count);

   printf("And what's the name? \n> ");

   read(0,input,count);

   if (memcmp(birdy,global_birdy,BIRDBUF)) {
      printf("*** Dangerous Stack Activity Detected *** : Are you messing with my Canary?!\n");
      exit(-1);
   }

   
   printf("Ok... its name is %s\n", input);
   fflush(stdout);
}


int main() {
	
	init();
  	carry_bird_into_mine();
	printf("Working in a coal mine is dangerous stuff. \nGood thing I've got my bird to protect me. \n");
	printf("Let give it a name.\n... \n");
	name_it();
	return 0;
}
