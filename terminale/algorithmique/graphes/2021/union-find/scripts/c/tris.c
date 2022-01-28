#include "find_union_perso.h"
#include "tris.h"

void tri_rapide(Arete **t, int deb, int fin) {
  if (fin > deb) {
    int pivot = deb;
    // place tous les plus petits avant le pivot
    for (int i = deb + 1; i <= fin; i++) {
      if (t[i]->poids < t[pivot]->poids) {
        Arete *en_cours = t[i];
        for (int j = i - 1; j >= pivot; j--) {
          t[j + 1] = t[j];
        }
        t[pivot] = en_cours;
        pivot++;
      }
    }
    tri_rapide(t, deb, pivot-1);
    tri_rapide(t, pivot+1, fin);
  }
}