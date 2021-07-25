#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int chercher(int *tab, int e, int taille) {
  /*
  renvoie la 1° position de e dans tab
  -1 sinon
  */
  for (int i = 0; i < taille; i++) {
    if (tab[i] == e) {
      return i;
    }
  }
  return -1;
}
int main(int argc, char *argv[]) {
  srand(time(NULL)); // init random

  int taille = 10;
  int *tab = malloc(10 * sizeof(int));
  for (int i = 0; i < taille; i++) {
    tab[i] = rand() % 12;
  }
  for (int i = 0; i < taille; i++) {
    printf("%d ", tab[i]);
  }
  printf("\n");
  printf("%d\n", chercher(tab, 10, taille));
}