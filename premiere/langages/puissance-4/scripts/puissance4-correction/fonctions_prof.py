#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 25 Novembre 2021 19:23
"""

from constantes import *


def changer_joueur(joueur: int) -> int:
    """
    passe la main à l'autre joueur

    Args:
        joueur (int): joueur en cours

    Returns:
        int: l'autre joueur
    """
    return joueur % 2+1


def afficher_gagnant(joueur: int) -> str:
    """
    crée la phrase pour le gagnant

    Args:
        joueur (int): le joueur gagnant

    Returns:
        str: la phrase
    """
    if joueur == ROUGE:
        couleur = "rouge"
    else:
        couleur = "jaune"
    return f"Le joueur {couleur} a gagné."


def choisir_colonne() -> int:
    """
    demande la colonne
    vérifie si c'est un nombre

    Returns:
        int: la colonne choisie
    """    
    while True:
        try:
            rep = int(input("Dans quelle colonne placez-vous le jeton? "))
            break
        except ValueError:
            print("Il faut un nombre")
    return rep
