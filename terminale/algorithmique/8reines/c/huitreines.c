#include <stdio.h>
#include <stdlib.h>
#define REINES 8

int placer(int *placements, int ligne) {
  if (ligne == REINES) {
    return 1;
  } else {
    for (int col = 0; col < REINES; col++) {
      int possible = 1;
      for (int k = 0; k < ligne; k++) {
        if (placements[k] == col || placements[k] + k == col + ligne ||
            placements[k] - k == col - ligne) {
          possible = 0;
        }
      }
      if (possible == 1) {
        placements[ligne] = col;
        if (placer(placements, ligne + 1) == 1) {
          return 1;
        }
      }
    }
    return 0;
  }
}

int main(int argc, char *argv[]) {
  int *placements = malloc(REINES * sizeof(int));
  placer(placements, 0);

  // affichage
  for (int i = 0; i < REINES; i++) {
    printf("%d %d\n", i, placements[i]);
  }
  return 0;
}