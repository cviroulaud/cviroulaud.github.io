#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 30 15:49:54 2020

@auteur: Christophe Viroulaud

fonctions définissant différents scénarios

"""


from random import randint

def une_ligne(g: list)->None:
    """
    oscillateur de 3 cellules

    Parameters
    ----------
    g : list
        la grille.

    Returns
    -------
    None

    """
    nb_cel = len(g)
    g[nb_cel//2][nb_cel//2] = True
    g[nb_cel//2+1][nb_cel//2] = True
    g[nb_cel//2+2][nb_cel//2] = True

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
        x,y = randint(0,199), randint(0,199)
        g[x][y] = True

def vaisseau(g: list, decalage: int)->None:
    """
    structure capable de produire une copie d'elle-même mais décalée

    Parameters
    ----------
    g : list
        la grille.
    decalage : int
        l'abscisse de départ.

    Returns
    -------
    None

    """
    g[2][0+decalage] = True
    g[0][1+decalage] = True
    g[2][1+decalage] = True
    g[1][2+decalage] = True
    g[2][2+decalage] = True

def canon(g: list)->None:
    """
    lanceur de vaisseaux

    Parameters
    ----------
    g : list
        la grille.

    Returns
    -------
    None

    """
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

def escalier(g: list)->None:
    """
    structure qui se stabilise

    Parameters
    ----------
    g : list
        La grille.

    Returns
    -------
    None

    """
    nb_cel = len(g)
    g[nb_cel//2][nb_cel//2] = True
    g[nb_cel//2+1][nb_cel//2] = True
    g[nb_cel//2+1][nb_cel//2-1] = True
    g[nb_cel//2+2][nb_cel//2-1] = True
    g[nb_cel//2+2][nb_cel//2-2] = True
    g[nb_cel//2+3][nb_cel//2-2] = True