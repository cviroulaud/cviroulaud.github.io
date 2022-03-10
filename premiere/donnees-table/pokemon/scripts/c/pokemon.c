#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct pokemon pokemon;
struct pokemon {
  int num;
  char nom[30];
  char type[30];
  float height;
  char adr[50];
  float weight;
  char dist[20];
  char weaknesses[30];
  int next_evolution;
};

int main(int argc, char *argv[]) {
  FILE *f = NULL;
  char *token;
  f = fopen("pokedex.csv", "r");
  if (f == NULL) {
    printf("erreur");
  } else {
    char line[1024];
    while (fgets(line, 1024, f)) {
      token = strtok(line, ",");

      while (token != NULL) {
        printf("Token: %s\n", token);
        token = strtok(NULL, ",");
      }
    }
  }
  return 0;
}