#include "fonctions.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

Maillon *creer_liste(int t) {
  Maillon *premier = NULL;
  for (int i = 0; i < t; i++) {
    Maillon *m = malloc(sizeof(Maillon));
    m->val = rand() % 101;
    m->prec = premier;
    premier = m;
  }
  return premier;
}

int last(Maillon *l) {
  if (l->prec == NULL) {
    return l->val;
  } else {
    return last(l->prec);
  }
}

Maillon *reverse(Maillon *l, Maillon *suivant) {
  // en place
  if (l == NULL) {
    return suivant;
  } else {
    Maillon *temp = l->prec;
    l->prec = suivant;
    return reverse(temp, l);
  }
}

void reversed(Maillon **l) { 
    *l = reverse(*l, NULL); 
    //version 'en place' avec double pointeur
    //https://pythontutor.com/c.html#code=%23include%20%3Cstdio.h%3E%0A%23include%20%3Cstdlib.h%3E%0A%23include%20%3Ctime.h%3E%0A%23define%20taille%205%0A%0Atypedef%20struct%20Maillon%20Maillon%3B%0Astruct%20Maillon%20%7B%0A%20%20int%20val%3B%0A%20%20struct%20Maillon%20*prec%3B%0A%7D%3B%0AMaillon%20*creer_liste%28int%20t%29%20%7B%0A%20%20Maillon%20*premier%20%3D%20NULL%3B%0A%20%20for%20%28int%20i%20%3D%200%3B%20i%20%3C%20t%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20Maillon%20*m%20%3D%20malloc%28sizeof%28Maillon%29%29%3B%0A%20%20%20%20m-%3Eval%20%3D%20rand%28%29%20%25%20101%3B%0A%20%20%20%20m-%3Eprec%20%3D%20premier%3B%0A%20%20%20%20premier%20%3D%20m%3B%0A%20%20%7D%0A%20%20return%20premier%3B%0A%7D%0A%0AMaillon%20*reverse%28Maillon%20*l,%20Maillon%20*suivant%29%20%7B%0A%20%20//%20en%20place%0A%20%20if%20%28l%20%3D%3D%20NULL%29%20%7B%0A%20%20%20%20return%20suivant%3B%0A%20%20%7D%20else%20%7B%0A%20%20%20%20Maillon%20*temp%20%3D%20l-%3Eprec%3B%0A%20%20%20%20l-%3Eprec%20%3D%20suivant%3B%0A%20%20%20%20return%20reverse%28temp,%20l%29%3B%0A%20%20%7D%0A%7D%0A%0Avoid%20reversed%28Maillon%20**l%29%20%7B%20*l%20%3D%20reverse%28*l,%20NULL%29%3B%20%7D%0A%0Aint%20main%28%29%20%7B%0Asrand%28time%28NULL%29%29%3B%0A%20%20Maillon%20*liste%20%3D%20creer_liste%28taille%29%3B%0A%20%20reversed%28%26liste%29%3B%0A%20%20return%200%3B%0A%7D&curInstr=69&mode=display&origin=opt-frontend.js&py=c_gcc9.3.0&rawInputLstJSON=%5B%5D}

void affichage(Maillon *l) {
  Maillon *enc = l;
  for (int i = 0; i < taille; i++) {
    printf("%d ", enc->val);
    enc = enc->prec;
  }
  printf("\n");
}

int main(int argc, char *argv[]) {
  srand(time(NULL));
  Maillon *liste = creer_liste(taille);
  affichage(liste);
  printf("dernier %d\n", last(liste));
  reversed(&liste);
  affichage(liste);
  return 0;
}