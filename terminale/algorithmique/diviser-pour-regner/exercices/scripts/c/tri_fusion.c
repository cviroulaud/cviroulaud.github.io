#include "tri_fusion.h"

static void fusion(int *tab, int deb, int fin) {
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

void tri_fusion(int *tab, int d, int f) {
  if (d < f) {
    int m = (f + d) / 2;
    tri_fusion(tab, d, m);
    tri_fusion(tab, m + 1, f);
    fusion(tab, d, f);
  }
}