#include <stdio.h>
#include <stdlib.h>

void main()
{
    char str[100];

    printf("hello world !!!\n");
    printf("enter the string \n");
    fgets(str, 100, stdin);

    printf("the string is %s \n", str);
}