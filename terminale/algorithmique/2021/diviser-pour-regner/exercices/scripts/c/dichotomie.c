#include "tri_fusion.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define taille 10

int dicho(int *tab, int x) {
  // renvoie la position de x dans tab, -1 sinon
  int deb = 0;
  int fin = taille - 1;
  while (fin > deb) {
    int milieu = (fin + deb) / 2;
    if (tab[milieu] == x) {
      return milieu;
    } else if (x < tab[milieu]) {
      fin = milieu - 1;
    } else {
      deb = milieu + 1;
    }
  }
  return -1;
}

int main(int argc, char *argv[]) {
  srand(time(NULL));
  int *tab = malloc(taille * sizeof(tab));
  for (int i = 0; i < taille; i++) {
    tab[i] = rand() % 11; // 0 et 100
  }
  tri_fusion(tab, 0, taille - 1);
  // affichage
  for (int i = 0; i < taille; i++) {
    printf("%d ", tab[i]);
  }
  printf("\n");
  printf("%d\n", dicho(tab, 8));
  return 0;
}