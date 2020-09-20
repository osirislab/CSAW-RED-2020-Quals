#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <errno.h>

#define BUFSIZE 40
#define MAXINPUTSIZE 3
#define BSS 0x602000

char spellcode[BUFSIZE];

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

void countershell(){
    printf("Enter the offset do you wish to write to (0-39): > ");
    fflush(stdout);
    int offset = getIntClean();
    if (offset < 0 || offset >= BUFSIZE){
        printf("Invalid offset.\n");
        exit(0);
    }
    printf("Enter the modified byte: > ");
    fflush(stdout);
    int code_length = read(0, &spellcode[offset], 1);

    // check that the string length hasn't changed
    if(strlen(spellcode)==BUFSIZE){
        void (*runthis)() = (void (*)()) spellcode;
        runthis();
    }
    else{
        exit(0);
    }
}

void init(){
    setvbuf(stdout, NULL, _IONBF, 0);
    //errno = 0;
    //0x602000
    int protection_result = mprotect((char *)BSS, 1024, PROT_EXEC | PROT_READ | PROT_WRITE);
    //int protection_result = mprotect(&shellcode, BUFSIZE, PROT_EXEC | PROT_READ | PROT_WRITE);
    //printf("protection result: %d",protection_result);
    //printf("Error number: %s", strerror(errno)); // https://www.gnu.org/software/libc/manual/html_node/Error-Messages.html
    strncpy(spellcode, "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x48\x83\xec\x08\xe9\x13\xeb\xdf\xff\x00",40);
        //\xff\xff\xdf\xeb\xd5\x00",40);
        //\x90\x90\x90\x90\x90\x00",40);
}

void runGame(){
    printf("-----------------------");
    printf("Choose a spell to cast:\n");
    printf("   1)   Lightning Bolt\n");
    printf("   2)   Dispel Magic\n");
    printf("   3)   Counterspell\n");
    printf(">");
    fflush(stdout);
    int selection = getIntClean();
    if (selection == 1){
        puts("   Your lightning bolt strikes the challenge server!");
        puts("It explodes in a shower of sparks and challenges go everywhere.");
        puts("Maybe that wasn't a good ide--");
        exit(0);
    }
    else if(selection == 2){
        puts("   That's a great spell but the magic has to take effect first");
        puts("for you to dispel it...");
        puts("   You are banished! You look up from your keyboard.");
        exit(0);
    }
    else if (selection == 3){
        puts("Yes!! Time for some countershellcode.\n");
        puts("   As the admin's magic streaks towards you, you fall backwards,");
        puts("Matrix style, read the spellcode with your disassembler glasses,");
        puts("and modify a single byte of the spellcode in the air...");
        puts("");
        countershell();
    }
    else
    {
        puts("Error: invalid selection.");
        exit(0);
    }
    return;
}


int main(int argc, char **argv){
    puts("*** Level 3 Spellcoding ***\n");
    puts("   Welcome to Level 3! Clearing the doors, you take a right and get a view of Brooklyn from");
    puts("ten floors up. Room 1066 is the OSIRIS lab. Not Jeff, the skeleton sitting in a chair by the door,");
    puts("\"greets\" you as you walk in. He is wearing badges from previous CSAW years, and a CSAW 2020 badge.");
    puts("   Time to snag a CSAW 2020 badge! Wait a minute...an admin sees you as you fail a stealth check.");
    puts("Before you can think, the admin casts Modify Memory, a 5th-level spell!");
    init();
    puts("   The admin seems to be preparing a Banishment spell next. You have only a split second to react.\n");
    runGame();
    return 0;
}


