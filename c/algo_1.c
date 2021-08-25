#include <stdlib.h>
#include <stdio.h>

void main()
{
    int *p_array, iterators;

    printf("Q1:  Write an algorithm to produce the first 15 numbers of this series: 1,1,2,3,5,8,13,21…\n");

    printf("Enter the number  of iterators: ");
    scanf("%d", &iterators);

    p_array = (int *)malloc(sizeof(int) * iterators); // allocate 50 ints

    for (int i = 0; i < iterators; i++)
    {
        if (i >= 2)
        {
            int current_value = p_array[i - 2] + p_array[i - 1];
            p_array[i] = current_value;
            printf("sequenc value: %d\n", current_value);
        }
        else
        {
            p_array[i] = 1;
            printf("sequenc value: %d\n", 1);
        }
        // p_array[i] = i + 1;
    }
}
