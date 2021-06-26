#include "fonctions_tris.h"

void tri_selection(int *tab) {
  for (int i = 0; i < taille; i++) {
    int i_maxi = 0;
    for (int j = 1; j < taille - i; j++) {
      if (tab[i_maxi] < tab[j]) {
        i_maxi = j;
      }
    }
    // inversion
    int temp = tab[taille - i - 1];
    tab[taille - i - 1] = tab[i_maxi];
    tab[i_maxi] = temp;
  }
}

void tri_insertion(int *tab) {
  for (int i = 0; i < taille; i++) {
    int en_cours = tab[i];
    int j = i;
    while (j > 0 && tab[j - 1] > en_cours) {
      tab[j] = tab[j - 1];
      j--;
    }
    tab[j] = en_cours;
  }
}

// tri fusion
void fusionner(int *tab, int deb, int fin) {
  int *res = malloc((fin - deb + 1) * sizeof(int));
  int milieu = (fin + deb) / 2;
  // tab est trié entre deb et m et entre m+1 et fin
  int i = deb, j = milieu + 1, k = 0;
  while (i <= milieu && j <= fin) {
    if (tab[i] < tab[j]) {
      res[k] = tab[i];
      i++;
    } else {
      res[k] = tab[j];
      j++;
    }
    k++;
  }
  // fin des tab
  for (int i1 = i; i1 <= milieu; i1++) {
    res[k] = tab[i1];
    k++;
  }
  for (int j1 = j; j1 <= fin; j1++) {
    res[k] = tab[j1];
    k++;
  }
  // remet la partie de tab dans l'ordre
  for (int k1 = 0; k1 <= (fin - deb); k1++) {
    tab[deb + k1] = res[k1];
  }
  free(res);
}

void tri_fusion(int *tab, int deb, int fin) {
  if (fin - deb > 0) {
    int milieu = (fin + deb) / 2;
    tri_fusion(tab, deb, milieu);
    tri_fusion(tab, milieu + 1, fin);
    fusionner(tab, deb, fin);
  }
}

// tri rapide
void permuter(int *tab, int pos1, int pos2) {
  int temp = tab[pos1];
  tab[pos1] = tab[pos2];
  tab[pos2] = temp;
}

int partitionner(int *tab, int deb, int fin) {
  int pivot = tab[deb];
  int pos = deb;
  /*place tous les inférieurs à pivot de 1 à pos
  et tous les supérieurs de pos à fin
  */
  for (int i = deb + 1; i <= fin; i++) {
    if (tab[i] < pivot) {
      pos++;
      permuter(tab, i, pos);
    }
  }
  // place le pivot (en 0) au bon endroit (sa position finale dans tab)
  permuter(tab, pos, deb);
  return pos;
}

void tri_rapide(int *tab, int deb, int fin) {
  if (fin - deb > 0) {
    int pivot = partitionner(tab, deb, fin);
    tri_rapide(tab, deb, pivot - 1);
    tri_rapide(tab, pivot + 1, fin);
  }
}