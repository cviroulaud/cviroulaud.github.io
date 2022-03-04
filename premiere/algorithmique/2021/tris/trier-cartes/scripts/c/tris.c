#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define taille 20

void affichage(int *tab) {
  for (int i = 0; i < taille; i++) {
    printf("%d - ", tab[i]);
  }
}

void inserer(int *tab, int j) {
  while (j >= 0 && tab[j] < tab[j - 1]) {
    int temp = tab[j];
    tab[j] = tab[j - 1];
    tab[j - 1] = temp;
    j = j - 1;
  }
}
void tri_insertion(int *tab) {
  for (int i = 0; i < taille; i++) {
    inserer(tab, i);
  }
}

int main(int argc, char *argv[]) {
  srand(time(NULL));
  int *tab = malloc(taille * sizeof(tab));
  for (int i = 0; i < taille; i++) {
    tab[i] = rand() % 101;
  }
  affichage(tab);
  printf("\n");
  tri_insertion(tab);
  affichage(tab);
  return 0;
}