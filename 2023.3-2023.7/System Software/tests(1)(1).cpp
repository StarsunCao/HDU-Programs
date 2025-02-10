#define DOCTEST_CONFIG_IMPLEMENT
#include <string.h>
#include <iostream>
#include "../producer_consumer.h"
#include "doctest.h"
int main(int argc, char** argv) {
  //  doctest::Context context;
  //  context.applyCommandLine(argc, argv);
  //
  //  int res = context.run(); // run doctest
  //
  //  // important - query flags (and --exit) rely on the user doing this
  //  if (context.shouldExit())
  //  {
  int sum;

  int debug = 0;
  const char* debugStr = "_debug";
  if (argc > 3) {
    char* str = argv[3];
    if (!strcmp(debugStr, str)) {
      debug = 1;
    }
  }
  int number = 0;
  int sleep = 0;
  if (argc == 2) {
    number = atoi(argv[1]);
    sleep = 0;
  }
  if (argc > 3) {
    number = atoi(argv[1]);
    sleep = (int)(atoi(argv[2]) / 1000);
  } else {
    std::cin >> number;
    std::cin >> sleep;
  }
  sum = run_threads(debug, number, sleep);
  printf("%d\n", sum);
  // propagate the result of the tests
  //    return res;
  //  }

  return 0;
}
// TEST_CASE("test") {
//  int sum=run_threads(1);
// std::cout<<sum;
//}
