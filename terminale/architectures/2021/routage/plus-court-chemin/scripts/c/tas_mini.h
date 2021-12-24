#ifndef DEF_TRIS // Si la constante n'a pas été définie le fichier n'a jamais
                 // été inclus
#define DEF_TRIS // On définit la constante pour que la prochaine fois le
                 // fichier ne soit plus inclus

typedef struct Noeud Noeud;
struct Noeud {
  int nom;
  int distance;
  Noeud *prec;
};

typedef struct {
  int capacite;
  int dernier; // dernier indice libre
  Noeud **tab; // tableau de Noeud
} Tas;

Tas *init_tas(int c);
void enfiler(Tas *t, int nom, int dist);
Noeud *defiler(Tas *t);

#endif