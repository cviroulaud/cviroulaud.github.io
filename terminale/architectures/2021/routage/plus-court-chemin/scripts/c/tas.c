#include "tas.h"
#include <stdio.h>
#include <stdlib.h>

Tas *init_tas(int c) {
  Tas *t = malloc(sizeof(Tas));
  if (t == NULL) {
    exit(0);
  }
  t->tab = malloc(c * sizeof(t->tab));
  if (t->tab == NULL) {
    exit(0);
  }
  t->capacite = c;
  t->dernier = 0;
  return t;
}

void agrandir(Tas *t) {
  // double la capacité du tas
  if (t->dernier == t->capacite) {
    int n_cap = 2 * t->capacite;
    t->tab = realloc(t->tab, n_cap * sizeof(t->tab));
    if (t->tab == NULL) {
      exit(0);
    }
    t->capacite = n_cap;
  }
}
void enfiler(Tas *t, int val) {
  agrandir(t); // vérifie la capacité et agrandis si besoin
  // on insère par le bas et on remonte
  int fils = t->dernier;
  t->tab[fils] = val;
  int pere = (fils - 1) / 2;
  // remonte l'élément dans le tas
  while (t->tab[fils] > t->tab[pere]) {
    int temp = t->tab[fils];
    t->tab[fils] = t->tab[pere];
    t->tab[pere] = temp;

    fils = pere;
    pere = (pere - 1) / 2;
  }
  t->dernier = t->dernier + 1;
}

static int get_fils_maxi(Tas *t, int ind) {
  int maxi = 2 * ind + 1;
  // renvoie l'indice du fils maxi
  if (maxi > t->dernier) { // il n'y a pas de fils
    return -1;
  }
  if (maxi == t->dernier) { // il n'y a pas de fils droit
    return maxi;
  }
  if (t->tab[maxi] < t->tab[maxi + 1]) {
    maxi = maxi + 1;
  }
  return maxi;
}

int defiler(Tas *t) {
  int elt = t->tab[0]; // le plus grand est le premier
  // remonter le dernier à la racine
  t->tab[0] = t->tab[t->dernier - 1];
  t->dernier = t->dernier - 1;

  // faire redescendre sur le plus grand fils
  int en_cours = 0;
  int fils_maxi = get_fils_maxi(t, 0);
  while (fils_maxi > 0 || t->tab[en_cours] < t->tab[fils_maxi]) {
    int temp = t->tab[en_cours];
    t->tab[en_cours] = t->tab[fils_maxi];
    t->tab[fils_maxi] = temp;

    en_cours = fils_maxi;
    fils_maxi = get_fils_maxi(t, en_cours);
  }

  return elt;
}

static void afficher(Tas *t) {
  for (int i = 0; i < t->dernier; i++) {
    printf("%d ", t->tab[i]);
  }
  printf("\n");
}
int main() {
  Tas *tas = init_tas(100);
  enfiler(tas, 12);
  enfiler(tas, 11);
  enfiler(tas, 14);
  enfiler(tas, 8);
  enfiler(tas, 13);
  enfiler(tas, 7);
  enfiler(tas, 18);
  enfiler(tas, 6);
  enfiler(tas, 1);
  enfiler(tas, 10);
  enfiler(tas, 3);

  int s;
  while (tas->dernier > 0) {
    s = defiler(tas);
    afficher(tas);
    printf("%d\n", s);
  }
}