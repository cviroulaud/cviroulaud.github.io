#ifndef inclusion
#define inclusion

#define nb_noeuds 9
#define nb_aretes 14

typedef struct Noeud Noeud;
struct Noeud {
  struct Noeud *parent;
  int rang;
};

typedef struct Arete Arete;
struct Arete {
  int src, dest, poids;
};

Arete *creer_arete(int s, int d, int p);
void makeset(Noeud *n);
Noeud *find_perso(Noeud *n);
void union_perso(Noeud *n1, Noeud *n2);

#endif