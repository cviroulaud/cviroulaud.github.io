#ifndef DEF_TRIS // Si la constante n'a pas été définie le fichier n'a jamais
                 // été inclus
#define DEF_TRIS // On définit la constante pour que la prochaine fois le
                 // fichier ne soit plus inclus

/* Contenu de votre fichier .h (autres include, prototypes, define...) */
#define taille 6
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void tri_selection(int *tab);
void tri_insertion(int *tab);
void tri_fusion(int *tab, int deb, int fin);
void tri_rapide(int *tab, int deb, int fin);
#endif