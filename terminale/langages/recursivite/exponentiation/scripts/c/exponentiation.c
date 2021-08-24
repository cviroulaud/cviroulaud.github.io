#include <stdio.h>
#include <stdlib.h>

int exponentiation(int x, int n) {
  if (n == 0) {
    return 1;
  } else {
    return x*exponentiation(x, n - 1);
  }
}

int main(int argc, char *argv[]) {
  printf("%d\n", exponentiation(6, 4));
  return 0;
}