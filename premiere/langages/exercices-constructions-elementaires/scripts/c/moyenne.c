#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  float somme = 0;
  int nb= 2;
  float note = 0;
  for (int i = 0; i < nb; i++) {
    scanf("%f", &note);
    somme = somme + note;
  }
  printf("Moyenne: %f\n",somme/nb);
}