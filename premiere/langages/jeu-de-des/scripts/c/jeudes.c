#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
  srand(time(NULL));
  int de1 = rand() % 6 + 1;
  int proposition = 0;
  int nb_chance = 0;
  while (proposition != de1) {
    nb_chance++;
    printf("Choisir: ");
    scanf("%d", &proposition);
  }
  printf("Gagné en %d coups.\n", nb_chance);
  return 0;
}