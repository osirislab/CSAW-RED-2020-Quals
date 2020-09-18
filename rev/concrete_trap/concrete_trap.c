#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int stage1()
{
    char target[] = "u_will_never_guess_this_because_its_so_long";
    char input[0x30] = {};

    puts("What is my super secret passcode?");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;

    return !strcmp(target, input);
}

////

int stage2()
{
    int a = 0, b = 0;

    puts("What are my two numbers?");
    scanf("%d %d", &a, &b);

    if (a < 50 || b < 50)
        return 0;

    int result = a;
    for (int i = b; i > 0; --i)
    {
        result = (result ^ i*a+b);
    }
    //unrolled: a = a ^ (ab)+b ^ a(b-1)+b ^ ... ^ a+b

    return result == 31337;
}

int stage3()
{
    int a,b,c,d,e;

    puts("Even I haven't figured this one out yet");
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);

    for (int i = 0; i < 5; ++i)
    {
        a = b >> c + d*a;
        b = d << e - a*d;
        c = e >> a + c*b;
        d = b << c - e*d;
        e = c >> d + b*e;
    }

    if (a+b+c+d+e == 31337)
        return 1;
    return 0;
    //return a+b+c+d == 31337;
}

void give_flag()
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


void fail()
{
    puts("Wrong!");
    exit(0);
}

void init()
{
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main()
{
    init();

    puts("Welcome to my intricate trap, where all who are not me shall fail.");
    if (!stage1())
        fail();

    puts("I am slightly convinced you are me. Proceed.");

    if (!stage2())
        fail();

    puts("There are only a couple bazillion pairs of numbers I like. You might be me.");

    if (!stage3())
        fail();

    puts("Amazing");
    give_flag();

    return 0;
}
