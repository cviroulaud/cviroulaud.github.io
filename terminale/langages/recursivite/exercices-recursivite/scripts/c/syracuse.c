#include <stdio.h>
#include <stdlib.h>

void syracuse(int u, int *l, int pos) {
  l[pos] = u;
  if (u > 1) {
    if (u % 2 == 0) {
      syracuse(u / 2, l, pos + 1);
    } else {
      syracuse(3 * u + 1, l, pos + 1);
    }
  }
}

int main(int argc, char *argv[]) {
  int *tab = malloc(100 * sizeof *tab);
  syracuse(5, tab, 0);
  // les éléments sont forcément >0
  int i = 0;
  while (i<100 && tab[i]>0) {
  printf("%d ",tab[i]);
  i++;
  }
  return 0;
}  