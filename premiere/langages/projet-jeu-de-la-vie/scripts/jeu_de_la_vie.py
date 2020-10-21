#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 16 15:10:02 2020

@auteur: Christophe Viroulaud
"""


from tkinter import *
from random import randint

TAILLE = 8
CELLULES = 200

def compter_voisins(g: list, cel: tuple)->int:
    nb = 0
    delta = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    for decalage in delta:
        ligne, colonne = cel[0]+decalage[0], cel[1]+decalage[1]
        if ligne >= 0 and ligne < CELLULES and colonne >= 0 and colonne < CELLULES:
            if g[ligne][colonne]:
                nb += 1
    return nb

def cycle(f, c, g: list)->None:
    #global fenetre, grille
    nouvelle = [[False for _ in range(CELLULES)] for _ in range(CELLULES)]

    for i in range(CELLULES):
        for j in range(CELLULES):
            nb_voisins = compter_voisins(g, (i, j))

            if not g[i][j]: # une cellule morte
                if nb_voisins == 3: # devient vivante
                    nouvelle[i][j] = True
            else: # une cellule vivante
                if nb_voisins == 2 or nb_voisins == 3: # le reste
                    nouvelle[i][j] = True

    # la grille est actualisée
    g = nouvelle

    # affichage de la grille
    c.delete("all")
    for i in range(CELLULES):
        for j in range(CELLULES):
            if g[i][j]:
                c.create_oval(TAILLE*(j),
                                    TAILLE*(i),
                                    TAILLE*(j+1),
                                    TAILLE*(i+1),
                                    fill="blue")

    # nouveau cycle
    fenetre.after(100, cycle, f, c, g)

"""
programme principal
initialisation de la fenêtre graphique
"""
fenetre = Tk()
fenetre.title("Jeu de la vie")
canevas = Canvas(fenetre, width = CELLULES*TAILLE, height = CELLULES*TAILLE)
canevas.pack()

"""
initialisation de l'état de départ
"""
grille = [[False for _ in range(CELLULES)] for _ in range(CELLULES)]

"""
fonctions définissant différents scénarios
"""
def une_ligne(g: list)->None:
    g[CELLULES//2][CELLULES//2] = True
    g[CELLULES//2+1][CELLULES//2] = True
    g[CELLULES//2+2][CELLULES//2] = True

def aleatoire(g: list, n: int)->None:
    for _ in range(n):
        x,y = randint(0,199), randint(0,199)
        g[x][y] = True

def vaisseau(g: list, decalage: int)->None:
    g[2][0+decalage] = True
    g[0][1+decalage] = True
    g[2][1+decalage] = True
    g[1][2+decalage] = True
    g[2][2+decalage] = True

def canon(g: list)->None:
    g[7][4] = True
    g[8][4] = True
    g[7][5] = True
    g[8][5] = True
    g[7][14] = True
    g[8][14] = True
    g[9][14] = True
    g[6][15] = True
    g[10][15] = True
    g[5][16] = True
    g[11][16] = True
    g[5][17] = True
    g[11][17] = True
    g[8][18] = True
    g[6][19] = True
    g[10][19] = True
    g[7][20] = True
    g[8][20] = True
    g[9][20] = True
    g[8][21] = True
    g[5][24] = True
    g[6][24] = True
    g[7][24] = True
    g[5][25] = True
    g[6][25] = True
    g[7][25] = True
    g[4][26] = True
    g[8][26] = True
    g[3][28] = True
    g[4][28] = True
    g[8][28] = True
    g[9][28] = True
    g[5][38] = True
    g[6][38] = True
    g[5][39] = True
    g[6][39] = True


#une_ligne(grille)
#aleatoire(grille, 3000)
#vaisseau(grille, 0)
"""
for i in range(20):
    vaisseau(grille, 10*i)
"""
canon(grille)

cycle(fenetre, canevas, grille)

fenetre.mainloop()