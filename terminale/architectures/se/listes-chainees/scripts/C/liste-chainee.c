#include <stdio.h>
#include <stdlib.h>

typedef struct maillon maillon;
struct maillon {
  int val;
  maillon *suiv;
};

maillon *ajouter(maillon *l, int val) {
  maillon *n = malloc(sizeof(maillon));
  n->val = val;
  n->suiv = l;
  return n;
}

int main(int argc, char *argv[]) {
  maillon *liste = NULL;
  liste = ajouter(liste, 1);
  liste = ajouter(liste, 2);

  return 0;
}