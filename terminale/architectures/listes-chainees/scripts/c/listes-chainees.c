#include "elements.h"
#include <stdio.h>
#include <stdlib.h>

Liste *initialisation() {
  Liste *liste = malloc(sizeof(*liste));

  if (liste == NULL) {
    exit(EXIT_FAILURE);
  }

  return liste;
}

void insertion(Liste *l, int nb) {
  Element *element = malloc(sizeof(*element));

  if (element == NULL) {
    exit(EXIT_FAILURE);
  }

  element->nb = nb;
  element->suivant = l->premier; // NULL si premier elt
  l->premier = element;
}

void affichage(Liste *l) {
  if (l != NULL) {
    Element *e = l->premier;
    while (e != NULL) {
      printf("%d\n", e->nb);
      e = e->suivant;
    }
  }
}
int main(int argc, char *argv[]) {
  Liste *ma_liste = initialisation();
  insertion(ma_liste, 2);
  insertion(ma_liste, 3);
  insertion(ma_liste, 7);

  affichage(ma_liste);
  return 0;
}