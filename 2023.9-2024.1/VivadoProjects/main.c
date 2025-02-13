#include "xil_io.h"

#define SIZE 100

void matrix_sub(int a[SIZE], int b[SIZE], int result[SIZE]) {
	for(int i=0; i<SIZE; i++){
		result[i] = a[i] - b[i];
	}
}

void matrix_mul(int a[SIZE], int b[SIZE], int result[SIZE]) {
	for(int i=0; i<10; i++){
		for(int j=0; j<10; j++){
			result[i*10+j] = 0;
			for(int k=0; k<10; k++){
				result[i*10+j] += a[i*10+k] * b[k*10+j];
			}
		}
	}
}

int main(){
	int a[SIZE] = {
			1,1,4,5,1,4,1,1,4,5,
			1,1,4,5,1,4,1,1,4,5,
			1,1,4,5,1,4,1,1,4,5,
			1,1,4,5,1,4,1,1,4,5,
			1,1,4,5,1,4,1,1,4,5,
			1,1,4,5,1,4,1,1,4,5,
			1,1,4,5,1,4,1,1,4,5,
			1,1,4,5,1,4,1,1,4,5,
			1,1,4,5,1,4,1,1,4,5,
			1,1,4,5,1,4,1,1,4,5

	};

	int b[SIZE] = {
			1,9,1,9,8,1,0,1,9,1,
			1,9,1,9,8,1,0,1,9,1,
			1,9,1,9,8,1,0,1,9,1,
			1,9,1,9,8,1,0,1,9,1,
			1,9,1,9,8,1,0,1,9,1,
			1,9,1,9,8,1,0,1,9,1,
			1,9,1,9,8,1,0,1,9,1,
			1,9,1,9,8,1,0,1,9,1,
			1,9,1,9,8,1,0,1,9,1,
			1,9,1,9,8,1,0,1,9,1
	};

	int c[SIZE] = {0};
	int d[SIZE] = {0};

	Xil_Out16(0x40000000, 0xFFFF);

	matrix_sub(a, b, c);
	matrix_mul(a, c, d);

	Xil_Out16(0x40000000, 0x5555);

	for(int i=0; i<SIZE; i++){
		Xil_Out16(0x40000000, d[i]);
	}

	while(1);
	return 0;
}
