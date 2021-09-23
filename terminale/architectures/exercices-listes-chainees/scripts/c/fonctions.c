#include "fonctions.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

Maillon *creer_liste(int t) {
  Maillon *premier = NULL;
  for (int i = 0; i < t; i++) {
    Maillon *m = malloc(sizeof(Maillon));
    m->val = rand() % 101;
    m->prec = premier;
    premier = m;
  }
  return premier;
}

void affichage(Maillon *l) {
  Maillon *enc = l;
  for (int i = 0; i < taille; i++) {
    printf("%d ", enc->val);
    enc = enc->prec;
  }
}
int main(int argc, char *argv[]) {
  srand(time(NULL));
  Maillon *liste = creer_liste(taille);
  affichage(liste);
  return 0;
}