#include <stdlib.h>
#include <stdio.h>

// fuction declearation for the factorail function
long int factorial(int n);

// void main function

void main()
{
    int n;
    printf("enter nunmber for the factorial");
    scanf("%d", &n);
    long int i = factorial(n);
    printf("the inputed number is %ld\n", i);
}

// factorail function for full calculation
long int factorial(int n)
{
    if (n >= 1)
    {
        return n * factorial(n - 1);
    }
    else
        return 1;
}