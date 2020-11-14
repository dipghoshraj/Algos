#include <stdlib.h>
#include <stdio.h>

// fuction declearation for the factorail function
int factorial(int n);

// void main function

void main()
{
    int n;
    printf("enter nunmber for the factorial");
    scanf("%d", &n);
    int i = factorial(n);
    printf("the inputed number is %d\n", i);
}

// factorail function for full calculation
int factorial(int n)
{
    n = n * 5;
    return n;
}