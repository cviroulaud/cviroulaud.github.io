#include <stdio.h>
#include <stdlib.h>

typedef struct Maillon Maillon;
struct Maillon {
  int val;
  Maillon *suiv;
};

typedef struct File File;
struct File {
  Maillon *premier;
  Maillon *dernier;
};

void enfiler(File **f, int v) {
  Maillon *nouv = malloc(sizeof(Maillon));
  nouv->val = v;
  nouv->suiv = NULL;
  if ((*f)->premier == NULL) {
    (*f)->premier = nouv;
  } else {
    (*f)->dernier->suiv = nouv;
  }
  (*f)->dernier = nouv;
}

int defiler(File **f) {
  if ((*f)->premier == NULL) {
    return -1;
  } else {
    int res = (*f)->premier->val;
    (*f)->premier = (*f)->premier->suiv;
    return res;
  }
}

int main(int argc, char *argv[]) {
  File *f = malloc(sizeof(File));
  f->premier = NULL;
  f->dernier = NULL;
  enfiler(&f, 5);
  enfiler(&f, 6);
  printf("%d", defiler(&f));
  return 0;
}