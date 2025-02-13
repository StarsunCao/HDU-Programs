#include "xil_io.h"

#define AXI_GPIO_OUT_ADDR 0x40000000
#define AXI_GPIO_IN_ADDR 0x40000008

int getINValues() {
    int value = Xil_In16(AXI_GPIO_IN_ADDR);
    while ((value & 0x8000) == 0)
        value = Xil_In16(AXI_GPIO_IN_ADDR);
    value = value & 0x00FF;
    Xil_Out16(AXI_GPIO_OUT_ADDR, 0x4000);
    Xil_Out16(AXI_GPIO_OUT_ADDR, 0x0000);
    return value;
}

void OutputResule(int value) {
    value = (value & 0x00FF) | 0x8000;
    Xil_Out16(AXI_GPIO_OUT_ADDR, value);
    value = value & 0x7FFF;
    Xil_Out16(AXI_GPIO_OUT_ADDR, value);
}

int main() {
    int A[100];
    int B[100];
    int C[100] = {0};
    int D[100];

    for (int i = 0; i < 100; i++) {
        A[i] = getINValues();
    }

    for (int i = 0; i < 100; i++) {
        B[i] = getINValues();
    }

    for (int i = 0; i < 100; i++) {
    	D[i] = A[i] - B[i];
    }

    for(int i=0; i<10; i++){
    	for(int j=0; j<10; j++){
    		C[i*10+j] = 0;
    		for(int k=0; k<10; k++){
    			C[i*10+j] += A[i*10+k] * D[k*10+j];
    		}
    	}
    }


    for (int i = 0; i < 100; i++) {
        OutputResule(C[i]);
    }

    while (1);

    return 0;
}
