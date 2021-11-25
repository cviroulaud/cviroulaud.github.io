#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 25 Novembre 2021 19:26
"""
from constantes import *


def verif_gagnant(grille: list, joueur: int, ligne: int, colonne: int) -> bool:
    """
    Vérifie si la position est gagnante

    Args:
        grille (list): le jeu
        joueur (int): la couleur du joueur
        ligne (int): ligne du dernier jeton
        colonne (int): colonne du dernier jeton

    Returns:
        bool: True si la position est gagnante
    """    
    if verif_verticale(grille, joueur, ligne, colonne) or \
            verif_horizontale_droite(grille, joueur, ligne, colonne) or \
            verif_horizontale_gauche(grille, joueur, ligne, colonne):
        return True
    else:
        return False


def verif_verticale(grille: list, joueur: int, ligne: int, colonne: int) -> bool:
    """
    vérifie si l'alignement vertical est gagnant

    Args:
        grille (list): le jeu
        joueur (int): la couleur en cours
        ligne (int): la ligne du dernier jeton placé
        colonne (int): la colonne du dernier jeton placé

    Returns:
        bool: True si gagnant
    """
    compteur = 0
    while ligne < HAUTEUR and grille[ligne][colonne] == joueur and compteur < 4:
        compteur = compteur+1
        ligne = ligne+1
    # si 4 jetons alignés renvoie True
    return compteur == 4


def verif_horizontale_droite(grille: list, joueur: int, ligne: int, colonne: int) -> bool:
    """
    vérifie si l'alignement horizontal vers la droite est gagnant

    Args:
        grille (list): le jeu
        joueur (int): la couleur en cours
        ligne (int): la ligne du dernier jeton placé
        colonne (int): la colonne du dernier jeton placé

    Returns:
        bool: True si gagnant
    """
    compteur = 0
    while colonne < LARGEUR and grille[ligne][colonne] == joueur and compteur < 4:
        compteur = compteur+1
        colonne = colonne+1
    # si 4 jetons alignés renvoie True
    return compteur == 4


def verif_horizontale_gauche(grille: list, joueur: int, ligne: int, colonne: int) -> bool:
    """
    vérifie si l'alignement horizontal vers la gauche est gagnant

    Args:
        grille (list): le jeu
        joueur (int): la couleur en cours
        ligne (int): la ligne du dernier jeton placé
        colonne (int): la colonne du dernier jeton placé

    Returns:
        bool: True si gagnant
    """
    compteur = 0
    while colonne >= 0 and grille[ligne][colonne] == joueur and compteur < 4:
        compteur = compteur+1
        colonne = colonne-1
    # si 4 jetons alignés renvoie True
    return compteur == 4
