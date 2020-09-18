#include <stdio.h>
#include <stdlib.h>

int f(int x, int* y) {
    if (x % 2 != 0) {
        return x;
    }
    (*y)++;
    return f(x/2, y);
}

int main() {

    int a=0, b=0, c=24, d=6, e=0;
    char input[d];
    char buff[c];
    FILE *fp = NULL;
    
    printf("Enter a number from 1 to 99999:\n");  
    fgets(input, d, stdin);
    e = atoi(input);
    
    if (e > 0)
        a = f(e, &b);

    if ( b == 7 && (a+b) == c-d) {
        fp = fopen("flag.txt","r");
        fgets(buff, c, fp);
        printf("%s\n", buff);
    } else {
        printf("Nope, that's not it.\n");
    }

    return 0;
}