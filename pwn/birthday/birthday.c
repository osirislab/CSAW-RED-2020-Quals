#include <stdio.h>
#include <stdlib.h>

void init()
{
    setvbuf(stdout, NULL, _IONBF, 0);
}

typedef struct Birthday
{
    int day;
    int month;
    int year;
} Birthday;

int days[365] = {};

void full_version()
{
    char buf[0x80];
    FILE *f;
    f = fopen("flag.txt", "r");
    if (f != NULL)
    {
        fgets(buf, sizeof(buf), f);
        printf("Flag: %s\n", buf);
    } else
    {
        printf("Missing flag.txt. If you're running this on the server, please message an admin\n");
    }
}

void play()
{
    puts("Having trouble keeping track of birthdays? We got the tool for you!\n");
    for (int i = 0; i < 2; ++i)
    {
        int x;
        Birthday b;

        printf("How many of your acquaintances share this birthday? ");
        scanf("%d", &x);

        printf("When is your acquaintances birth year? ");
        scanf("%d", &b.year);

        printf("When is your acquaintances birth month? ");
        scanf("%d", &b.month);

        printf("When is your acquaintances birth day? ");
        scanf("%d", &b.day);

        days[b.month * 30 + b.day] = x;
    }
    puts("Thanks for using the free trial. Buy the full version to add more friends and get reminded when its their birthday!");
}

int main()
{
    init();
    play();

    return 0;
}
