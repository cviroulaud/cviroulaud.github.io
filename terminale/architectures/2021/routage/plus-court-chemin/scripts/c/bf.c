#include <stdio.h>
#include <stdlib.h>
#define dist_max 1000
#define nb 6

typedef struct Sommet {
  int dist;
  int pred;
} Sommet;
/*
AUTRE MÉTHODE
Sommet **distances = malloc(3 * sizeof(distances));
for (int i = 0; i < 3; i++) {
    Sommet *s = malloc(sizeof(Sommet));
    distances[i]=s;
    distances[i]->dist = 100;
    distances[i]->pred = NULL;
}
*/

// ou void bf(int mat[nb][nb], int d, int a) {
// ou void bf(int mat[][nb], int d, int a) {
void bf(int (*mat)[nb], int d, int a) {
  Sommet *distances = malloc(nb * sizeof(Sommet));
  for (int i = 0; i < nb; i++) {
    distances[i].dist = dist_max;
    distances[i].pred = -1;
  }
  distances[0].dist = 0;

  int modif = 1;
  while (modif == 1) {
    modif = 0;
    for (int i = 0; i < nb; i++) {
      for (int j = 0; j < nb; j++) {
        if (mat[i][j] != 0) {
          int dist_calc = mat[i][j] + distances[i].dist;
          if (dist_calc < distances[j].dist) {
            distances[j].dist = dist_calc;
            distances[j].pred = i;
            modif = 1;
          }
        }
      }
    }
  }
  
  // reconstruction (à l'envers)
  while (a != d) {
    printf("%d ", a);
    a = distances[a].pred;
  }
  printf("%d", d);
}

int main(int argc, char *argv[]) {
  int mat[nb][nb] = {{0, 10, 0, 0, 0, 8},  {0, 0, 0, 2, 0, 0},
                     {0, 2, 0, 0, 0, 0},   {0, 0, -2, 0, 0, 0},
                     {0, -4, 0, -1, 0, 0}, {0, 0, 0, 0, 1, 0}};

  bf(mat, 0, 3);
  return 0;
}