#include "SNN.h"

void elementry_multiplication(double *weight, double input, double *output_vector, int LABLES_COUNT) {
	// EM_result = W1*i/p + W2*i/p + W3*i/p + ....... +  Wn*i/p (W = weight, i/p = input;
	for (int i = 0; i < LABLES_COUNT; i++) {
		output_vector[i] = input * weight[i];
	}
}

void SIMO(double* weight, double input, double* output_vector, int LABLES_COUNT) {
	// single input single output NN;
	elementry_multiplication(weight, input, output_vector, LABLES_COUNT);
}
