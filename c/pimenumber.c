#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPrime(int n);

void main()
{
    int n = 3;
    printf("hello world !!");

    bool pime = isPrime(n);
    printf("%d \n", pime);
}

bool isPrime(int n)
{
    int lastdigit = n / 10;
    if (lastdigit == 5)
        return false;
    if (lastdigit % 2 != 0)
        return false;

    else
    {
        if (lastdigit % 3 != 0 || lastdigit % 7 != 0 || lastdigit % 9 != 0)
            return false;
        else
            return true;
    }

    return false;
}
