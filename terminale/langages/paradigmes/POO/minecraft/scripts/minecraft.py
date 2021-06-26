#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/24 18:14:41
"""
from random import shuffle
from constantes import *
from blocs import *
from outils import *
from joueur import Joueur
from moteur import Moteur

# lancement du moteur de jeu
moteur = Moteur()

# création des blocs
grille = [None for _ in range(LARGEUR*HAUTEUR)]
for i in range(0, 100):
    grille[i] = Obsidienne()
for i in range(100, 300):
    grille[i] = Terre()
for i in range(300, 900):
    grille[i] = Roche()

shuffle(grille)

# création de 15 outils stocké dans un dictionnaire
outils_poses = {}
# associe des coordonnées à un outil: la clé est le tuple de coordonnées
for i in range(5):
    outils_poses[moteur.donner_coordonnees()] = Pioche("wood_pickaxe")
    outils_poses[moteur.donner_coordonnees()] = Pioche("diamond_pickaxe")
    outils_poses[moteur.donner_coordonnees()] = Pelle()

# commencer
joueur = Joueur("Christophe")
moteur.commencer(joueur, grille, outils_poses)
