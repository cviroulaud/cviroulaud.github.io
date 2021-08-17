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

def aleatoire(g: list, n: int)->None:
    """
    place n cellules au hasard

    Parameters
    ----------
    g : list
        la grille.
    n : int
        le nombre de cellules à placer.

    Returns
    -------
    None

    """
    for _ in range(n):
        x,y = randint(0,CELLULES-1), randint(0,CELLULES-1)
        g[x][y] = True

def compter_voisins(g: list, cel: tuple)->int:
    """
    compte les voisins d'une cellule

    Parameters
    ----------
    g : list
        la grile.
    cel : tuple
        la cellule en cours.

    Returns
    -------
    int
        le nombre de voisins.

    """
    nb = 0
    delta = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    for decalage in delta:
        ligne, colonne = cel[0]+decalage[0], cel[1]+decalage[1]
        if ligne >= 0 and ligne < CELLULES and colonne >= 0 and colonne < CELLULES:
            if g[ligne][colonne]:
                nb += 1
    return nb

def cycle(f, c, g: list)->None:
    """
    crée un nouveau cycle

    Parameters
    ----------
    f : TYPE
        fenêtre tkinter.
    c : TYPE
        caneva tkinter.
    g : list
        grille du jeu.

    Returns
    -------
    None

    """
    # crée une nouvelle grille de cellules mortes
    nouvelle = # À COMPLÉTER

    for i in range(CELLULES):
        for j in range(CELLULES):
            # compte les voisins de la cellule (i,j)
            nb_voisins = # À COMPLÉTER

            # respecte les règles du jeu
            # À COMPLÉTER

    # la grille est actualisée
    g = nouvelle

    # affichage de la grille
    affichage(f, c, g)

    # nouveau cycle: la méthode after rappelle la fonction cycle toutes les 100ms
    f.after(100, cycle, f, c, g)

def affichage(f, c, g: list)->None:
    """
    gestion de l'affichage
    """
    c.delete("all")
    for i in range(CELLULES):
        for j in range(CELLULES):
            if g[i][j]:
                c.create_oval(TAILLE*(j),
                                    TAILLE*(i),
                                    TAILLE*(j+1),
                                    TAILLE*(i+1),
                                    fill="blue")


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
aleatoire(grille, 3000)

"""
lancement du jeu
"""
cycle(fenetre, canevas, grille)
fenetre.mainloop()
