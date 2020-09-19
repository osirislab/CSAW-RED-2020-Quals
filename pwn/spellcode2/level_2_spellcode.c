#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

#define BUFSIZE 40
#define MAXINPUTSIZE 2

// This binary was compiled with an executable stack
// To do this yourself, use gcc -m32 -z execstack -fno-pie -no-pie 

void getInput(int length, char * buffer){
    memset(buffer, 0, length);
    int count = 0;
    char c;
    while((c = getchar()) != '\n' && !feof(stdin)){
        if(count < (length-1)){
            buffer[count] = c;
            count++;
        }
    }
    buffer[count] = '\x00'; 
}

int getIntClean(){
    char input[MAXINPUTSIZE]; 
    getInput(MAXINPUTSIZE, input);
    return atoi(input);
}

void runGame(){
    char shellcode[BUFSIZE];
    printf("Choose a spell to cast:\n");
    printf("   1)   Continual Flame\n");
    printf("   2)   Knock\n");
    printf("   3)   Misty Step\n");
    printf("   4)   Shatter\n");
    printf("   5)   Suggestion\n");
    printf(">");
    fflush(stdout);
    int selection = getIntClean();
    if (selection == 1){
        puts("You flame the Discord channel!!\n");
        puts("This spell is way too overpowered for second level...");
        puts("I'm sorry, I think you just set off every alarm in the");
        puts("building.");
        exit(0);
    }
    else if(selection == 2){
        puts("Your knock spell causes the door to fly open.");
        puts("But it was alarmed!");
        exit(0);
    }
    else if (selection == 3){
        puts("Good idea, but I forget how to cast that spell.");
        puts("Can you remind me?\n");
        printf("Enter your spell code (up to %d bytes): > ", BUFSIZE);
        fflush(stdout);
        // Make sure there is something to run
        int code_length = read(0, shellcode, BUFSIZE);
        // Put some null bytes in the middle of the shellcode
        //char* write_location = &shellcode;
        //write_location += 12;
        int zeros = open("/dev/zero", O_RDONLY);
        read(zeros, &shellcode[12],5);
        if(code_length > 0){
            void (*runthis)() = (void (*)()) shellcode;
            runthis();
        }
    }
    else if (selection == 4){
        puts("   Your spell shatters the doors and the stack!");
        int garbage = open("/dev/random", O_RDONLY);
        read(garbage, &shellcode,150);
    }
    else if (selection == 5){
        puts("   You cast Suggestion...okay, try casting Misty Step.\n");
        runGame();
    }
    else
    {
        puts("Error: invalid selection.");
        exit(0);
    }
    return;
}

int main(int argc, char **argv){
    setvbuf(stdout, NULL, _IONBF, 0);
    puts("*** Level 2 Spellcoding ***\n");
    puts("   You proceed to the 370 Jay Street elevators and");
    puts("level up! You can now cast level 2 spells. You");
    puts("reach Floor 10, and the OSIRIS lab is nearby.");
    puts("But first you must enter the Center for Cyber");
    puts("Security through a set of glass doors that blocks");
    puts("your path forward. A card reader is set to check");
    puts("your student ID, so you need to bypass it.");
    puts("");
    runGame();
    printf("\n");
    return 0;
}


