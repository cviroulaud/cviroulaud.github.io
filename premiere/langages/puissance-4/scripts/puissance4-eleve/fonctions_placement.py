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
    return ...


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
    return ...


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
    # récupère où le jeton doit "tomber"
    ligne = ...
    # met à jour la grille: place le jeton du joueur
    ...
    # renvoie la ligne
    return ...


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
    # on descend tant qu'on n'est pas en bas ou sur une case remplie
    while ... and ...:
        ligne = ligne + 1

    # renvoie la dernière place vide
    return ligne-1
