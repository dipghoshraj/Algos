#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char *encrypt(const char *);

void main()
{
    char *str;

    printf("hello world !!!\n");
    printf("enter the string \n");

    str = (char *)malloc(50 * sizeof(char));
    scanf("%s", str);

    printf("%s\n", str);
}

const char *encrypt(char str[100])
{
    return "encrypt";
}

const char *decrypt(char str[100])
{
    return "decrypt";
}