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

void empiler(Liste *l, int nb) {
  Element *element = malloc(sizeof(*element));

  if (element == NULL) {
    exit(EXIT_FAILURE);
  }

  element->nb = nb;
  element->suivant = l->premier; // NULL si premier elt
  l->premier = element;
}

int depiler(Liste *l) {
  if (l == NULL) {
    exit(EXIT_FAILURE);
  }
  int nb = l->premier->nb;
  l->premier = l->premier->suivant;
  return nb;
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
  Liste *pile = initialisation();
  empiler(pile, 2);
  empiler(pile, 3);
  empiler(pile, 7);

  affichage(pile);

  printf("dépile: %d\n", depiler(pile));

  affichage(pile);
  return 0;
}