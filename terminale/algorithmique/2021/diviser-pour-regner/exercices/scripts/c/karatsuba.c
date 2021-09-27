#include <stdio.h>
#include <stdlib.h>

int puissance(int x, int n) {
  if (n == 0) {
    return 1;
  } else if (n % 2 == 0) {
    return puissance(x * x, n / 2);
  } else {
    return x * puissance(x * x, n / 2);
  }
}

int kara(int m1, int m2, int n) {
  if (n == 1) {
    return m1 * m2;
  } else {
    int k = n / 2;
    int a = m1 / puissance(10, k);
    int b = m1 % puissance(10, k);
    int c = m2 / puissance(10, k);
    int d = m2 % puissance(10, k);
    int a0 = kara(a, c, n / 2);
    int a2 = kara(b, d, n / 2);
    int a1 = kara(a - b, c - d, n / 2);
    return a0 * puissance(10, 2 * k) + (a0 + a2 - a1) * puissance(10, k) + a2;
  }
}

int main(int argc, char *argv[]) {
  printf("%d\n", kara(1237, 2587, 4));
  return 0;
}