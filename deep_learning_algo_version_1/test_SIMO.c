#include <stdio.h>
#include <stdlib.h>

#include "SNN.h"
//
//#define LABLE_COUNT = 2;
//#define temprature[] = {20, 25, 31, 54, 32, 15}
//#define humidity[] = {1.5, 2.5, 3.1, 5.4, 3.2, 1.5}
//
//#define weiht[] = {2, 0.5}


#define sad 0.9
#define TEMP_IDX 0
#define HUMIDITY_IDX 1

#define LABLE_COUNT 2

double out_vector[2];
double weight[] = { 2, 1 };

double test_SIMO() {
	SIMO(weight, sad, out_vector, LABLE_COUNT);
	printf("predicted value is %f ", out_vector[TEMP_IDX]);
}