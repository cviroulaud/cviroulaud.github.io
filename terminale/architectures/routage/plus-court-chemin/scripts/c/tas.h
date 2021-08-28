#ifndef DEF_TRIS // Si la constante n'a pas été définie le fichier n'a jamais
                 // été inclus
#define DEF_TRIS // On définit la constante pour que la prochaine fois le
                 // fichier ne soit plus inclus

typedef struct {
  int capacite;
  int dernier;//dernier indice libre
  int *tab;
} Tas;

typedef struct Noeud Noeud;
struct Noeud {
  int nom;
  int distance;
  Noeud *prec;
} ;

#endif