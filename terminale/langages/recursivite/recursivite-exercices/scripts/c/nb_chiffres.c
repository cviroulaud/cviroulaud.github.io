#include <stdio.h>
#include <stdlib.h>

int nb_chiffres(int n) {
  if (n < 10) {
    return 1;
  } else {
    return 1 + nb_chiffres(n / 10);
  }
}

int nb_chiffres_terminale(int n, int acc) {
  if (n < 10) {
    return acc;
  } else {
    return nb_chiffres_terminale(n / 10, acc + 1);
  }
}

int main(int argc, char *argv[]) {
  printf("nb_chiffres %d\n", nb_chiffres(1234));
  printf("nb_chiffres_terminale %d\n", nb_chiffres_terminale(1234, 1));
}