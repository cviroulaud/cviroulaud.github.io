#include <stdio.h>
#include <stdlib.h>

void division_rec(int dividende, int diviseur, int *q, int *r);

void division_rec(int dividende, int diviseur, int *q, int *r) {
  if (dividende < diviseur) {
    *r = dividende;
  } else {
    *q = *q + 1;
    division_rec(dividende - diviseur, diviseur, q, r);
  }
}

int main(int argc, char *argv[]) {
  int q = 0;
  int r;
  division_rec(23, 5, &q, &r);
  printf("%d %d\n", q, r);

  q = 0;
  division_rec(25, 5, &q, &r);
  printf("%d %d\n", q, r);
}