#include <stdio.h>
#include <stdlib.h>

typedef struct pile {
  int val;
  struct pile *pred;
} Pile;

//juste
void empiler(Pile **p, int i) {
  Pile *p_new = malloc(sizeof(Pile));
  if (p_new != NULL) {
    p_new->val = i;
    p_new->pred = *p;
    *p = p_new;
  }
}

//incorrect
void empiler2(Pile *p, int i) {
  Pile *p_new = malloc(sizeof(Pile));
  if (p_new != NULL) {
    p_new->val = i;
    p_new->pred = p;
    p = p_new;
  }
}

int main(int argc, char *argv[]) {
  Pile *p = malloc(sizeof(Pile));
  empiler(&p, 3);
  empiler(&p, 4);
  // printf("%d\n", p->val);
  Pile *e = p;
  int i = 0;
  while (e != NULL) {
    printf("%d %d\n", i, e->val);
    e = e->pred;
    i++;
  }

  Pile *p2 = malloc(sizeof(Pile));
  empiler2(p2, 5);
  empiler2(p2, 6);
  Pile *e2 = p2;
  int i2 = 0;
  while (e2 != NULL) {
    printf("%d %d\n", i2, e2->val);
    e2 = e2->pred;
    i2++;
  }
}