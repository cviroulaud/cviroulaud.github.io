#include <stdio.h>
#include <stdlib.h>

const int taille = 8;
void dec_to_bin(unsigned int x, int bin_rev[]) {
  /*
  donne le code binaire (sur 8 bits)
  d'un entier positif
  */
  // initialisation
  int bin_inter[taille];
  for (int i = 0; i < taille; i++) {
    bin_inter[i] = 0;
  }
  // calculs bits
  int i = 0;
  while (x != 0) {
    bin_inter[i] = x % 2;
    x = x / 2;
    i++;
  }
  // reverse
  for (int j = taille - 1; j >= 0; j--) {
    bin_rev[taille - j - 1] = bin_inter[j];
  }
}

void dec_to_bin_rec(unsigned int x) {
  /*
  version récursive
  */
  if (x == 1) {
    printf("%d", x);
  } else {
    int reste = x % 2;
    dec_to_bin_rec(x / 2);
    printf("%d", reste);
  }
}

unsigned int horner(int binaire[], int taille) {
  int res = 0;
  int i = 0;
  while (i < taille) {
    res = res * 2 + binaire[i];
    i++;
  }
  return res;
}

int main(int argc, char *argv[]) {
  dec_to_bin_rec(35);
  printf("\n");
  int binaire[8] = {0};
  dec_to_bin(35, binaire);
  for (int i = 0; i < taille; i++) {
    printf("%d", binaire[i]);
  }
  printf("\n");
  int bin_nb[8] = {0, 0, 1, 0, 0, 0, 1, 1};
  printf("%d", horner(bin_nb, sizeof(bin_nb) / sizeof(bin_nb[0])));
  printf("\n");
  return 0;
}