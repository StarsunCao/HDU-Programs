#include <string.h>
#include <iostream>
#include "producer_consumer.h"

int main(int argc, char** argv) {
  int sum;
  int number = 0;
  int sleep = 0;
  int debug = 0;
  const char* debugStr = "_debug";
  if (argc > 3) {
    char* str = argv[3];
    if (!strcmp(debugStr, str)) {
      debug = 1;
    }
  }
  if (argc == 2) {
    number = atoi(argv[1]);
    sleep = 0;
  } else {
    number = atoi(argv[1]);
    sleep = (int)(atoi(argv[2]) / 1000);
  }
  sum = run_threads(debug, number, sleep);
  printf("%d\n", sum);
  return 0;
}
