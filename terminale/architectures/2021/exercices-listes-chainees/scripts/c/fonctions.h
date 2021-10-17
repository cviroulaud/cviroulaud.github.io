#define taille 5
typedef struct Maillon Maillon;
struct Maillon {
  int val;
  struct Maillon *prec;
};