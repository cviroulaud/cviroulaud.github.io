#include <stdio.h>
#include <stdlib.h>
#define nb 6

typedef struct Objet {
  int poids;
  int valeur;
} Objet;

void affichage(int *t, int l, int c) {
  for (int i = 0; i < l; i++) {
    for (int j = 0; j < (c + 1); j++) {
      printf("%d ", t[i * (c+1) + j]);
    }
    printf("\n");
  }
}
int main(int argc, char *argv[]) {
  Objet *objets = malloc(nb * sizeof(Objet));
  objets[0].valeur = 0;
  objets[0].poids = 0;
  objets[1].valeur = 1;
  objets[1].poids = 2;
  objets[2].valeur = 2;
  objets[2].poids = 5;
  objets[3].valeur = 3;
  objets[3].poids = 7;
  objets[4].valeur = 7;
  objets[4].poids = 12;
  objets[5].valeur = 10;
  objets[5].poids = 9;

  int poids_max = 15;
  // initialisation du tableau des calculs des valeurs
  int *solutions = malloc((poids_max + 1) * nb * sizeof(int));
  for (int i = 0; i < (poids_max + 1) * nb; i++) {
    solutions[i] = 0;
  }

  for (int j = 1; j < (poids_max + 1); j++) {
    for (int i = 1; i < nb; i++) {
      int prend_pas = solutions[(i - 1) * (poids_max+1) + j];
      if (objets[i].poids <= j) {
        int prend =
            solutions[(i - 1) * (poids_max+1) + (j - objets[i].poids)] + objets[i].valeur;
        if (prend > prend_pas) {
          solutions[i * (poids_max+1) + j] = prend;
        } else {
          solutions[i * (poids_max+1) + j] = prend_pas;
        }
      } else {
        solutions[i * (poids_max+1) + j] = prend_pas;
      }
    }
  }

  affichage(solutions, nb, poids_max);
  printf("%d\n", solutions[(nb - 1) * nb + poids_max + 1]);
  return 0;
}