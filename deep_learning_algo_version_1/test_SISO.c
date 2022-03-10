#include "SNN.h"
#include "test_SNN.h"

double test_SISO() {
	double temprature[2] = { 12, 5 };
	double  weight = -1;
	return SISO(temprature[0], weight);
}