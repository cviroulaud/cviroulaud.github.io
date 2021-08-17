#include "elements.h"


Liste *initialisation() {
  Liste *liste = malloc(sizeof(Liste));

  if (liste == NULL) {
    exit(EXIT_FAILURE);
  }

  return liste;
}

void initialisation2(Liste *l) { l = malloc(sizeof(Liste)); }

void insertion(Liste *l, int nb) {
  Element *element = malloc(sizeof(Element));

  if (element == NULL) {
    exit(EXIT_FAILURE);
  }

  element->nb = nb;
  element->suivant = l->premier; // NULL si premier elt
  l->premier = element;
}

void affichage(Liste *l) {
  int i = 0;
  if (l != NULL) {
    Element *e = l->premier;
    while (e != NULL) {
      printf("%d %d\n", i, e->nb);
      e = e->suivant;
      i++;
    }
  }
}
//v1 OK
/*
int main(int argc, char *argv[]) {
   Liste *ma_liste = initialisation();
  insertion(ma_liste, 2);
  insertion(ma_liste, 3);
  insertion(ma_liste, 7);

  affichage(ma_liste);
  return 0;
}
//v2 OK
int main(int argc, char *argv[]) {
  Liste *ma_liste = malloc(sizeof(Liste));
  insertion(ma_liste, 2);
  insertion(ma_liste, 3);
  insertion(ma_liste, 7);

  affichage(ma_liste);
  return 0;
}*/
//v3 NON
int main(int argc, char *argv[]) {
  Liste ma_liste;
  initialisation2(&ma_liste);
  insertion(&ma_liste, 2);
  insertion(&ma_liste, 3);
  insertion(&ma_liste, 7);

  affichage(&ma_liste);
  return 0;
}