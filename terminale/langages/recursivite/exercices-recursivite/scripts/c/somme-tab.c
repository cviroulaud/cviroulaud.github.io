#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define taille 10

void somme(int *tab, int *s, int i) {
  if (i < taille) {
    *s += tab[i];
    somme(tab, s, i + 1);
  }
}

int somme2(int *tab, int s, int i) {
  if (i < taille) {
    return somme2(tab, s + tab[i], i + 1);
  }
  return s;
}

int main(int argc, char *argv[]) {
  srand(time(NULL));
  int s = 0;
  int *t = malloc(taille * sizeof(int));
  for (int i = 0; i < taille; i++) {
    t[i] = rand() % 100 + 1; // entre 1 et 100 inclus
  }
  somme(t, &s, 0);
  for (int i = 0; i < taille; i++) {
    printf("%d ", t[i]);
  }
  printf("somme: %d\n", s);
  printf("somme: %d\n", somme2(t, 0, 0));

  return 0;
}