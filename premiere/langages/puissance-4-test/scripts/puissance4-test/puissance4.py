#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 25 Novembre 2021 12:27
"""
from constantes import *
from fonctions_prof import *
from fonctions_placement import *
from fonctions_verif import *
from moteur_turtle import *

# initialisation
grille = initialiser_grille(LARGEUR, HAUTEUR)
joueur = ROUGE
# affichage graphique
dessiner_grille(grille)

gagnant = False
while not gagnant:
    # demande la colonne choisie (tant qu'elle est pleine)
    remplie = True
    while remplie:
        colonne = choisir_colonne()
        remplie = est_remplie(grille, colonne)

    # place le jeton
    ligne = placer_jeton(grille, colonne, joueur)

    # vérifie si gagnant
    if verif_gagnant(grille, joueur, ligne, colonne):
        gagnant = True
        print(afficher_gagnant(joueur))
    else:
        # affichage graphique
        dessiner_jeton(grille, ligne, colonne)
        # au tour de l'autre joueur
        joueur = changer_joueur(joueur)
