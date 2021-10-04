#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
marche pas
http://igm.univ-mlv.fr/~dr/XPOSE2013/La_compression_de_donnees/arithm.html
*/
typedef struct Bornes {
  float inf, sup, proba;
} Bornes;

float arrondir(float var) {
  // 37.66666 * 100 =3766.66
  // 3766.66 + .5 =3767.16    for rounding off value
  // then type cast to int so value is 3767
  // then divided by 100 so the value converted into 37.67
  float value = (int)(var * 100 + .5);
  return (float)value / 100;
}

void creer_intervalles(char mot[], Bornes *intervalles) {
  int taille = strlen(mot);
  float frequences[256] = {0.};
  // comptage
  for (int i = 0; i < taille; i++) {
    frequences[mot[i]]++;
  }
  // calcul fréquences
  for (int i = 0; i < 256; i++) {
    frequences[i] = arrondir(frequences[i] / taille);
  }
  // calcul intervalles
  float borne = 0.;
  for (int i = 0; i < 256; i++) {
    if (frequences[i] > 0) {
      intervalles[i].inf = borne;
      intervalles[i].sup = borne + frequences[i];
      intervalles[i].proba = frequences[i];
      borne = intervalles[i].sup;
    } else {
      intervalles[i].inf = 0;
      intervalles[i].sup = 0;
    }
  }
}

Bornes codage(char mot[], Bornes *intervalles) {
  int taille = strlen(mot);
  Bornes code; // = malloc(sizeof(Bornes));
  code.inf = 0;
  code.sup = 1;
  for (int i = 0; i < taille; i++) {
    char lettre = mot[i];
    float t_inf = code.inf;
    float t_sup = code.sup;
    code.inf = t_inf + (t_sup - t_inf) * intervalles[lettre].inf;
    code.sup = t_inf + (t_sup - t_inf) * intervalles[lettre].sup;
  }
  return code;
}

void decodage(float code, Bornes *intervalles, char mot[]) {
  int j = 0;
  // marche pas: pb comparaison de float
  while (code > 0.001) {
    int i = 0;
    while (code > intervalles[i].sup) {
      i++;
    }
    mot[j] = i;
    j++;
    code = (code - intervalles[i].inf) / intervalles[i].proba;
  }
  mot[j]='\0';
}

int main(int argc, char *argv[]) {
  char mot[] = "ESIPE";

  Bornes *intervalles = malloc(256 * sizeof(Bornes));
  creer_intervalles(mot, intervalles);
  Bornes code = codage(mot, intervalles);
  printf("%f %f\n", code.inf, code.sup);
  char mot_decode[100];
  decodage(0.372, intervalles, mot_decode);
  printf("%s\n", mot_decode);
  return 0;
}