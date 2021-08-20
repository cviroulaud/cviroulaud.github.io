#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int demande(int de) {
  int proposition = 0;
  int nb_chance = 0;
  while (proposition != de) {
    nb_chance++;
    printf("Choisir: ");
    scanf("%d", &proposition);
  }
  return nb_chance;
}
int main(int argc, char *argv[]) {
  srand(time(NULL));
  int de1 = rand() % 6 + 1;
  printf("Gagné en %d coups.\n", demande(de1));
  return 0;
}