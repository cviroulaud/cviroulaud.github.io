#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 25 Novembre 2021 12:29
"""
from constantes import *


def initialiser_grille() -> list:
    """
    construire la grille du jeu

    Returns:
        list: un tableau de HAUTEUR lignes et LARGEUR colonnes
    """
    return [[VIDE for i in range(LARGEUR)] for j in range(HAUTEUR)]


def est_remplie(grille: list, colonne: int) -> bool:
    """
    vérifie si la colonne est remplie jusqu'en haut

    Args:
        grille (list): le jeu
        colonne (int): la colonne

    Returns:
        bool: True si la colonne est remplie
    """
    # il suffit de vérifier si l'emplacement le plus haut est vide
    return not(grille[0][colonne] == VIDE)


def placer_jeton(grille: list, colonne: int, joueur) -> int:
    """
    place le jeton 
    Args:
        grille (list): le jeu
        ligne (int): la ligne
        colonne (int): la colonne
        joueur ([type]): la couleur du joueur
    Returns:
        int: la ligne où le jeton s'est arrêté 
    """
    # vérification de la validité de la colonne
    assert colonne < LARGEUR, "La colonne est hors limite."

    ligne = tomber_ligne(grille, colonne)
    grille[ligne][colonne] = joueur
    return ligne


def tomber_ligne(grille: list, colonne: int) -> int:
    """
    fait descendre le jeton dans la colonne

    Args:
        grille(list): la grille de jeu
        colonne (int): la colonne choisie

    Returns:
        int: la ligne où le pion doit être placé
    """
    ligne = 0
    while ligne < HAUTEUR and grille[ligne][colonne] == VIDE:
        # on descend tant qu'on n'est pas en bas ou sur une case remplie
        ligne = ligne + 1

    # renvoie la dernière place vide
    return ligne-1


if __name__ == "__main__":
    # tests des préconditions des fonctions
    placer_jeton([], LARGEUR, 0)
