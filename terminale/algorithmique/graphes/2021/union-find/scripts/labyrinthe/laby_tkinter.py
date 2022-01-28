#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Date de création Fri Nov 13 22:21:39 2020

@auteur: Christophe Viroulaud
"""

import tkinter as tk
from constantes import *
from union_find import set_arbre_couvrant
from plus_court_chemin import bfs


fenetre = tk.Tk()
canevas = tk.Canvas(fenetre, width=largeur*taille, height=hauteur*taille)
canevas.pack()
"""
for x in range(largeur):
    canevas.create_line(x*taille, 0, x*taille, hauteur*taille)
for y in range(hauteur):
    canevas.create_line(0,y*taille, largeur*taille, y*taille)
"""

labyrinthe = set_arbre_couvrant()

# x et y sont les côtés gauche et haut des cellules
# murs verticaux
for y in range(hauteur):
    for x in range(largeur-1):
        # si pas d'arête entre les 2 cellules
        if ((x, y), (x+1, y)) not in labyrinthe and ((x+1, y), (x, y)) not in labyrinthe:
            canevas.create_line((x+1)*taille, (y)*taille,
                                (x+1)*taille, (y+1)*taille)

# murs horizontaux
for x in range(largeur):
    for y in range(hauteur-1):
        if ((x, y+1), (x, y)) not in labyrinthe and ((x, y), (x, y+1)) not in labyrinthe:
            canevas.create_line((x)*taille, (y+1)*taille,
                                (x+1)*taille, (y+1)*taille)

# plus court chemin
predecesseurs = bfs(labyrinthe)
noeud = (largeur-1, hauteur-1)  # en bas à droite
while predecesseurs[noeud] is not None:
    canevas.create_line((noeud[0]+.5)*taille, 
                        (noeud[1]+.5)*taille, 
                        (predecesseurs[noeud][0]+.5)*taille, 
                        (predecesseurs[noeud][1]+.5)*taille, 
                        fill="#FF0000", width=2)
    noeud = predecesseurs[noeud]
fenetre.mainloop()
