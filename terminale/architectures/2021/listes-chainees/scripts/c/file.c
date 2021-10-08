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

void enfiler(Liste *l, int nb) {
  Element *element = malloc(sizeof(*element));

  if (element == NULL) {
    exit(EXIT_FAILURE);
  }

  element->nb = nb;
  if (l->premier == NULL) {
    l->premier = element;
    l->dernier = l->premier; // = element
  } else {
    l->dernier->suivant = element;
    l->dernier = element;
  }
}

int defiler(Liste *l) {
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
      printf("%d <- ", e->nb);
      e = e->suivant;
    }
  }
}

int main(int argc, char *argv[]) {
  Liste *file = initialisation();
  enfiler(file, 2);
  enfiler(file, 3);
  enfiler(file, 4);
  enfiler(file, 7);

  affichage(file);

  printf("\ndéfile: %d\n", defiler(file));

  affichage(file);
  return 0;
}