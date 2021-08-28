#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

int factorielle(int x, int n) {
  assert(n >= 0);
  if (n == 0) {
    return 1;
  } else {
    return x * factorielle(x, n - 1);
  }
}

void fact2(int x, int n, int *res) {
  // avec un pointeur
  if (n != 0) {
    *res *= x;
    fact2(x, n - 1, res);
  }
}

int main(int argc, char *argv[]) {
  printf("%d\n", factorielle(2, 4));
  
  int r = 1;
  fact2(2, 4, &r);
  printf("%d\n", r);

  return 0;
}