#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
  srand(time(NULL));
  int nb = rand() % 10 + 1; // entre 1 et 10 inclus
  int p = 0;
  int essai = 0;
  while (p != nb) {
    essai++;
    scanf("%d", &p);
  }
  printf("%d essais", essai);
  return 0;
}
