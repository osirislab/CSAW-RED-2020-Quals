#include <stdio.h>
#include <string.h>
#include <sys/mman.h>

typedef unsigned char uchar;
typedef unsigned int uint;

void* initialize_mem(int size)
{
    void* addr = mmap(NULL, size, PROT_READ|PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    return addr;
}

uint *fetch_reg(uchar r)
{
    static uint a = 0;
    static uint b = 0;
    static uint c = 0;
    static uint d = 0;
    static uint e = 0;
    if (r == 'a')
        return &a;
    if (r == 'b')
        return &b;
    if (r == 'c')
        return &c;
    if (r == 'd')
        return &d;
    if (r == 'e')
        return &e;

    return NULL;
}


////////

/*
 * Program
 * encode:
 * movc a, 0
 * movr b, 86
 * put a, b
 * inc a
 * movr b, 33
 * put a, 33
 * inc a
 * movr b, 69
 * put a, 69
 * inc a
 * etc.
 *
 * decode:
 * mov a, 100
 * mov e, 0
 * mov d, 1
 *
 * get b, a ; mov b, [a]
 * movc c, 3
 * mul b, c
 * xor b, a
 * shrink b
 * get c, e
 * hrmpf d, b, c
 * inc a
 * inc e
 */

enum OPCODES
{
    NOP,
    MOVC,        //mov a, constant
    MOVR,       //mov a, b
    PUT,        //mov [a], b
    GET,        //mov a, [b]
    INC,
    DEC,
    MUL,
    SHRINK,     //and a, 0xff
    XOR,
    HRMPF,      //hrmpf d,a,b ; d && a==b //im sure theres a name for this but i cant remember
};

uchar fetch_1(uchar** stream)
{
    *stream += 1;
    uchar ret = **stream;
    return ret;
}

int run(uchar *mem)
{
    uchar program[] = {1, 97, 0, 1, 98, 86, 3, 97, 98, 5, 97, 1, 98, 33, 3, 97, 98, 5, 97, 1, 98, 69, 3, 97, 98, 5, 97, 1, 98, 82, 3, 97, 98, 5, 97, 1, 98, 25, 3, 97, 98, 5, 97, 1, 98, 46, 3, 97, 98, 5, 97, 1, 98, 250, 3, 97, 98, 5, 97, 1, 98, 44, 3, 97, 98, 5, 97, 1, 98, 194, 3, 97, 98, 5, 97, 1, 98, 8, 3, 97, 98, 5, 97, 1, 98, 247, 3, 97, 98, 5, 97, 1, 98, 114, 3, 97, 98, 5, 97, 1, 98, 72, 3, 97, 98, 5, 97, 1, 98, 237, 3, 97, 98, 5, 97, 1, 98, 16, 3, 97, 98, 5, 97, 1, 98, 234, 3, 97, 98, 5, 97, 1, 98, 105, 3, 97, 98, 5, 97, 1, 98, 23, 3, 97, 98, 5, 97, 1, 98, 229, 3, 97, 98, 5, 97, 1, 98, 33, 3, 97, 98, 5, 97, 1, 98, 36, 3, 97, 98, 5, 97, 1, 98, 38, 3, 97, 98, 5, 97, 1, 98, 230, 3, 97, 98, 5, 97, 1, 98, 63, 3, 97, 98, 5, 97, 1, 98, 239, 3, 97, 98, 5, 97, 1, 98, 19, 3, 97, 98, 5, 97, 1, 98, 231, 3, 97, 98, 5, 97, 1, 98, 41, 3, 97, 98, 5, 97, 1, 98, 157, 3, 97, 98, 5, 97, 1, 98, 29, 3, 97, 98, 5, 97, 1, 98, 222, 3, 97, 98, 5, 97, 1, 98, 158, 3, 97, 98, 5, 97, 1, 98, 188, 3, 97, 98, 5, 97, 1, 98, 21, 3, 97, 98, 5, 97, 1, 98, 193, 3, 97, 98, 5, 97, 1, 98, 30, 3, 97, 98, 5, 97, 1, 98, 255, 3, 97, 98, 5, 97, 1, 97, 100, 1, 101, 0, 1, 100, 1, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101, 4, 98, 97, 1, 99, 3, 7, 98, 99, 9, 98, 97, 8, 98, 4, 99, 101, 10, 100, 98, 99, 5, 97, 5, 101};

    uchar* opcodes = program;
    int len = sizeof(program);

    uchar *curr = opcodes;
    while (curr < opcodes+len)
    {
        if (*curr == NOP)
        {
        }
        else if (*curr == MOVC)
        {
            uchar one = fetch_1(&curr);
            uchar two = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);
            uint val2 = (uint)two;

            *reg1 = val2;
        }
        else if (*curr == MOVR)
        {
            uchar one = fetch_1(&curr);
            uchar two = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);
            uint *reg2 = fetch_reg(two);

            *reg1 = *reg2;
        }
        else if (*curr == PUT)
        {
            uchar one = fetch_1(&curr);
            uchar two = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);
            uint *reg2 = fetch_reg(two);

            mem[*reg1] = *reg2;
        }
        else if (*curr == GET)
        {
            uchar one = fetch_1(&curr);
            uchar two = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);
            uint *reg2 = fetch_reg(two);

            *reg1 = mem[*reg2];
        }
        else if (*curr == INC)
        {
            uchar one = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);

            *reg1 += 1;
        }
        else if (*curr == DEC)
        {
            uchar one = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);

            *reg1 -= 1;
        }
        else if (*curr == MUL)
        {
            uchar one = fetch_1(&curr);
            uchar two = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);
            uint *reg2 = fetch_reg(two);

            *reg1 *= *reg2;
        }
        else if (*curr == SHRINK)
        {
            uchar one = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);

            *reg1 &= 0xff;
        }
        else if (*curr == XOR)
        {
            uchar one = fetch_1(&curr);
            uchar two = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);
            uint *reg2 = fetch_reg(two);

            *reg1 ^= *reg2;
        }
        else if (*curr == HRMPF)
        {
            uchar one = fetch_1(&curr);
            uchar two = fetch_1(&curr);
            uchar three = fetch_1(&curr);
            uint *reg1 = fetch_reg(one);
            uint *reg2 = fetch_reg(two);
            uint *reg3 = fetch_reg(three);

            *reg1 = *reg1 && (*reg2 == *reg3);
        }
        curr += 1;
    }
    return *fetch_reg('d');
}

void play()
{
    char *mem = initialize_mem(200);
    printf("> ");
    fgets(mem+100, 50, stdin);

    if (run((uchar*)mem))
    {
        printf("yay\n");
    } else
    {
        printf(":(\n");
    }
}


int main()
{
    play();

    return 0;
}
