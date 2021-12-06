#include <stdio.h>
#include <stdlib.h>

typedef struct Pile Pile;
struct Pile {
  int val;
  Pile *prec;
};

void empiler(Pile **p, int val) {
  Pile *nouv = malloc(sizeof(Pile));
  if (nouv == NULL) {
    EXIT_FAILURE;
  }
  nouv->val = val;
  nouv->prec = *p;
  *p = nouv;
}

int depiler(Pile **p) {
  int x = -1;
  if (*p != NULL) {
    Pile *temp = (*p)->prec;
    x = (*p)->val;
    free(*p);
    *p = temp;
  }
  return x;
}

int main(int argc, char *argv[]) {
  Pile *p = NULL;
  empiler(&p, 5);
  printf("%d", depiler(&p));
  printf("%d", depiler(&p));

  return 0;
}