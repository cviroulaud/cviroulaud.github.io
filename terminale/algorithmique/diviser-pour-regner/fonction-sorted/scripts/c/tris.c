#include "fonctions_tris.h"

void affichage(int *tab) {
  for (int i = 0; i < taille; i++) {
    printf("%d ", tab[i]);
  }
  printf("\n");
}

int *creer_tableau() {

  int *tableau = malloc(taille * sizeof(int));
  for (int i = 0; i < taille; i++) {
    tableau[i] = rand() % 101; // entier entre 0 et 100
  }
  return tableau;
}

int main(int argc, char *argv[]) {
  srand(time(NULL)); // init random

  printf("Tri par sélection\n");
  int *tableau = creer_tableau();
  affichage(tableau);

  tri_selection(tableau);
  affichage(tableau);

  free(tableau);

  printf("Tri par insertion\n");
  tableau = creer_tableau();
  affichage(tableau);

  tri_insertion(tableau);
  affichage(tableau);

  free(tableau);

  printf("Tri à bulles\n");
  tableau = creer_tableau();
  affichage(tableau);

  tri_bulles(tableau);
  affichage(tableau);

  free(tableau);

  printf("Tri fusion\n");
  tableau = creer_tableau();
  affichage(tableau);

  tri_fusion(tableau, 0, taille - 1);
  affichage(tableau);

  free(tableau);

  printf("Tri rapide\n");
  tableau = creer_tableau();
  affichage(tableau);

  tri_rapide(tableau, 0, taille - 1);
  affichage(tableau);

  free(tableau);
}