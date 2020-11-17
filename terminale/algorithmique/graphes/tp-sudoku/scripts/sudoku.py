#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 16 11:20:57 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe
from graphviz import Graph
from math import sqrt
from random import shuffle

TAILLE = 4
grille = [[0 for _ in range(TAILLE)] for _ in range(TAILLE)]

g_sudoku = Graphe()
# création des sommets
for i in range(TAILLE):
    for j in range(TAILLE):
        g_sudoku.ajouter_sommet((j,i))

# arêtes verticales
for j in range(TAILLE):
    for i in range(TAILLE-1):
        for k in range(i+1, TAILLE):
            g_sudoku.ajouter_arete((j,i),(j,k))

# arêtes horizontales
for i in range(TAILLE):
    for j in range(TAILLE-1):
        for k in range(j+1, TAILLE):
            g_sudoku.ajouter_arete((j,i),(k,i))

# blocs
nb_blocs = int(sqrt(TAILLE))
# il y a (nb_blocs*nb_blocs) blocs
for bloc_lig in range(nb_blocs):
    for bloc_col in range(nb_blocs):
        # pour chaque case
        for i in range(nb_blocs):
            for j in range(nb_blocs):
                # vers chaque case
                for lig in range(nb_blocs):
                    for col in range(nb_blocs):
                        if not((j,i) == (col,lig)):
                            g_sudoku.ajouter_arete((bloc_col*nb_blocs+j, bloc_lig*nb_blocs+i),
                                                   (bloc_col*nb_blocs+col, bloc_lig*nb_blocs+lig))

#print(g_sudoku.get_sommets())
#print(g_sudoku.get_adjacents((1,1)))

def remplir(g: Graphe, grille: list):
    for s in g.get_sommets():
        # on n'utilise pas l'index 0!!!
        disponibles = [True for i in range(TAILLE+1)]
        for v in g.get_adjacents(s):
            # récupère le contenu de la case voisine
            case = grille[v[0]][v[1]]
            if case > 0: # si elle est déjà remplie
                # on élimine le chiffre disponible pour s
                disponibles[case] = False
            print(v[0],v[1],disponibles)
        # chiffres encore disponibles pour s
        restants = []
        for i in range(1,TAILLE+1):
            if disponibles[i]:
                restants.append(i)
        shuffle(restants)

        grille[s[0]][s[1]] = restants.pop()
        print(s[0],s[1],grille[s[0]][s[1]])

remplir(g_sudoku, grille)
print(grille)