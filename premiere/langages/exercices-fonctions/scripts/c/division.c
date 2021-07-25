#include <stdio.h>
#include <stdlib.h>

typedef struct resultat resultat;
struct resultat {
  int q;
  int r;
};

void division(int dividende, int diviseur, resultat *res) {
  res->q = 0;
  res->r = 0;
  while (dividende >= diviseur) {
    res->q = res->q + 1;
    dividende = dividende - diviseur;
  }
  res->r = dividende;
}

void division_rec(int dividende, int diviseur, resultat *res) {
  if (dividende >= diviseur) {
    res->q++;
    division_rec(dividende - diviseur, diviseur, res);
  } else {
    res->r = dividende;
  }
}

int main(int argc, char *argv[]) {
  resultat res;
  division(39, 5, &res);
  printf("%d %d\n", res.q, res.r);

  res.q = 0;
  res.r = 0;
  division_rec(39, 5, &res);
  printf("%d %d\n", res.q, res.r);

  return 0;
}