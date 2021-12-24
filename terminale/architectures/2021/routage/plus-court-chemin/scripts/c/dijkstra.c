#include "tas_mini.h"
#include <stdio.h>
#include <stdlib.h>
#define taille 10
#define dist_max 1000

int main(int argc, char *argv[]) {
  int graphe[taille][taille] = {
      {0, 6, 10, 0, 0, 0, 0, 0, 0, 0},   {0, 0, 0, 11, 14, 0, 0, 0, 0, 0},
      {0, 12, 0, 12, 0, 0, 8, 16, 0, 0}, {0, 0, 0, 0, 0, 6, 3, 0, 0, 0},
      {0, 0, 0, 0, 0, 4, 0, 0, 6, 0},    {0, 0, 0, 0, 0, 0, 0, 0, 12, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 16, 6},   {0, 0, 0, 0, 0, 0, 0, 0, 0, 8},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 13},   {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};

  /*
  tab_final permet de faire correspondre l'indice du tableau au nom du noeud
  dans non_visites l'indice change en fonction du defiler
  */
  // initialisation de tous les noeuds dans une file à priorité
  Tas *non_visites = init_tas(taille);
  Noeud **tab_final = malloc(taille * sizeof(tab_final));
  // Noeud **non_visites = malloc(taille * sizeof(non_visites));
  for (int i = 0; i < taille; i++) {
    enfiler(non_visites, i, dist_max);
    tab_final[i] = non_visites->tab[i];
  }
  // noeud de départ à 0
  /*rq (n'est plus d'actualité): le noeud 0 est forcément au début de la file à priorité
  par construction dans "enfiler" (à cause des inégalités strictes);
  sinon il faudrait "réarranger" la file comme dans "defiler"*/
  //non_visites->tab[0]->distance = 0;
  tab_final[0]->distance = 0;

  // 'visites' ne sert à rien: la file est déjà remplie
  Noeud **visites = malloc(taille * sizeof(visites));
  int ligne = 0; // pour ajouter dans "visites" et parcourir matrice

  while (non_visites->dernier > 0) {
    // récupère le noeud avec la plus petite distance
    // (= 1° de la file à priorité)
    Noeud *en_cours = defiler(non_visites);
    visites[ligne] = en_cours;

    // parcourt la matrice et compare les distances aux voisins
    for (int col = 0; col < taille; col++) {
      if (graphe[ligne][col] > 0) { // c'est un voisin
        int dist_calc = en_cours->distance + graphe[ligne][col];

        // compare distance actuelle du voisin avec celle calculée
        if (dist_calc < tab_final[col]->distance) {
          tab_final[col]->distance = dist_calc;
          tab_final[col]->prec = en_cours;
        }
      }
    }
    ligne++;
  }

  // affichage de toutes les distances
  for (int i = 0; i < taille; i++) {
    Noeud *n = tab_final[i];
    printf("noeud: %d, distance: %d\n", n->nom, n->distance);
  }
  // affichage du chemin le plus court depuis A (0)
  Noeud *n = tab_final[8];
  while (n->nom != 0) {
    printf("noeud: %d ", n->nom);
    n = n->prec;
  }
  printf("\n");
  return 0;
}
