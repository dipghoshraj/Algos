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
    else
        pime = isPrime(n);
    printf("%d \n", pime);
}

bool isPrime(int n)
{
    int lastdigit = n / 10;
    if (lastdigit == 5)
    {
        printf("five divied");
        return false;
    }
    if (n % 2 == 0)
    {
        printf("even number");
        return false;
    }

    else
    {
        if (n % 3 != 0 || n % 7 != 0 || n % 9 != 0)
        {
            printf("odd number");
            return true;
        }
        else
        {
            printf("odd non prime number");
            return false;
        }
    }

    return false;
}
