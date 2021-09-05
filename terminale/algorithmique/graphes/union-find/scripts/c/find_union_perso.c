#include "find_union_perso.h"
#include "tris.h"
#include <stdio.h>
#include <stdlib.h>

Arete *creer_arete(int s, int d, int p) {
  Arete *a = malloc(sizeof(Arete));
  a->src = s;
  a->dest = d;
  a->poids = p;
  return a;
}

void makeset(Noeud *n) {
  n->parent = n;
  n->rang = 0;
}

Noeud *find_perso(Noeud *n) {
  if (n->parent != n) {
    n->parent = find_perso(n->parent);
  }
  return n->parent;
}

void union_perso(Noeud *n1, Noeud *n2) {
  Noeud *r1 = find_perso(n1);
  Noeud *r2 = find_perso(n2);
  if (r1 != r2) {
    if (r1->rang > r2->rang) {
      r2->parent = r1;
    } else {
      r1->parent = r2;
      if (r1->rang == r2->rang) {
        r2->rang = r2->rang + 1;
      }
    }
  }
}

int main(int argc, char *argv[]) {
  // entrée des données
  Arete **aretes = malloc(10 * sizeof(Arete));
  aretes[0] = creer_arete(0, 1, 4);
  aretes[1] = creer_arete(0, 7, 8);
  aretes[2] = creer_arete(1, 2, 8);
  aretes[3] = creer_arete(1, 7, 11);
  aretes[4] = creer_arete(2, 3, 7);
  aretes[5] = creer_arete(2, 5, 4);
  aretes[6] = creer_arete(2, 8, 2);
  aretes[7] = creer_arete(3, 4, 9);
  aretes[8] = creer_arete(3, 5, 14);
  aretes[9] = creer_arete(4, 5, 10);
  aretes[10] = creer_arete(5, 6, 2);
  aretes[11] = creer_arete(6, 7, 1);
  aretes[12] = creer_arete(6, 8, 6);
  aretes[13] = creer_arete(7, 8, 7);

  // tri des arêtes pour Kruskal
  tri_rapide(aretes, 0, 13);
  // affichage des arêtes
  for (int i = 0; i < 14; i++) {
    printf("%c %c %d\n", aretes[i]->dest + 65, aretes[i]->src + 65,
           aretes[i]->poids);
  }

  Noeud *equivalence = malloc(nb_noeuds * sizeof(Noeud));
  for (int i = 0; i < nb_noeuds; i++) {
    makeset(&equivalence[i]);
  }
  // kruskal
  Arete **arbre_couvrant = malloc(nb_aretes * sizeof(Arete)); // au max 14 arêtes
  int next = 0;
  for (int i = 0; i < nb_aretes; i++) {
    int i1 = aretes[i]->src;
    int i2 = aretes[i]->dest;
    if (find_perso(&equivalence[i1]) != find_perso(&equivalence[i2])) {
      arbre_couvrant[next] = aretes[i];
      next++;
      union_perso(&equivalence[i1], &equivalence[i2]);
    }
  }
  // affichage
  printf("\n");
  for (int i = 0; i < next; i++) {
    printf("%c %c %d\n", arbre_couvrant[i]->dest + 65,
           arbre_couvrant[i]->src + 65, arbre_couvrant[i]->poids);
  }
  return 0;
}