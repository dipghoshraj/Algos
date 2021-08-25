// Write an algorithm to raise power of any value to any value

// begin
// define base
// define power
// Recursion condition power = 0,
//    base = base * base
// Next
// write base
// end

#include <stdlib.h>
#include <stdio.h>

// fuction declearation for the to_power function
float to_power(float base, float power);

void main()
{
    float base, power;
    printf("enter base::  ");
    scanf("%f", &base);

    printf("enter to_power::  ");
    scanf("%f", &power);

    float i = to_power(base, power);
    printf("Exponent value is %f\n", i);
}

float to_power(float base, float power)
{
    if (power > 0)
    {
        return base * to_power(base, power - 1);
    }
    else if (power < 0)
    {
        float positive_power = -(power);
        return 1.0 / (base * to_power(base, positive_power - 1));
    }
    else
    {
        return 1;
    }
}