#include <stdio.h>
#include <stdlib.h>
#define taille 3

void affichage(float *tab) {
  for (int i = 0; i < taille; i++) {
    printf("%f ", tab[i]);
  }
  printf("\n");
}

int main(int argc, char *argv[]) {
  float *notes = malloc(taille * sizeof(float));
  float somme = 0;
  for (int i = 0; i < taille; i++) {
    scanf("%f", &notes[i]);
    somme += notes[i];
  }
  affichage(notes);
  float moy = somme / taille;
  printf("\nMoyenne: %f\n", moy);
  if (moy > 15) {
    printf("Félicitations");
  } else if (moy > 10) {
    printf("Passable");
  } else {
    printf("Bof");
  }
}