#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPrime(int n);

void main()
{
    int n = 3;
    bool pime = false;
    printf("hello world  put your number here!!");
    scanf("%d", &n);

    if (n < 10)
    {
        if (n == 1 || n == 1 || n == 3 || n == 5 || n == 7)
            pime = true;
    }
    pime = isPrime(n);
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
