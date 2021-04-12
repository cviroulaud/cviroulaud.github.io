#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Date de création Fri Nov 13 22:21:39 2020

@auteur: Christophe Viroulaud
"""

import pygame
from pygame.locals import *

from constantes import *
from mod_labyrinthe import Labyrinthe
from parcours import dijkstra, a_star
from collections import deque


pygame.init()

fenetre = pygame.display.set_mode(
    (largeur*taille+bordure*2, hauteur*taille+bordure*2))

labyrinthe = Labyrinthe(fenetre)
depart = (6, 10)
arrivee = (20, 17)
# récupère chemin optimal et ordre de parcours des noeuds par Dijkstra
chemin_inverse, ordre = a_star(labyrinthe.laby, depart, arrivee)
chemin_affiche = []

pygame.key.set_repeat(400, 30)
continuer = True
while continuer:
    # Limitation de vitesse de la boucle
    pygame.time.wait(50)

    # progression des visites
    if ordre:
        en_cours = ordre.popleft()
        labyrinthe.laby[en_cours[1]][en_cours[0]].visite = True

    # affichage cellules
    fenetre.fill((255, 255, 255))
    labyrinthe.afficher_cellules()

    # départ et arrivée
    pygame.draw.rect(
        fenetre, RED, (depart[0]*taille+bordure+1, depart[1]*taille+bordure+1, taille-2, taille-2))
    pygame.draw.rect(
        fenetre, GREEN, (arrivee[0]*taille+bordure+1, arrivee[1]*taille+bordure+1, taille-2, taille-2))

    # quand parcours fini on affiche chemin
    if not ordre:
        if chemin_inverse:
            chemin_affiche.append(chemin_inverse.pop())
        for noeud in chemin_affiche:
            pygame.draw.rect(
                fenetre, RED, (noeud[0]*taille+bordure+1, noeud[1]*taille+bordure+1, taille-2, taille-2))

    # affichage murs
    labyrinthe.afficher_murs()

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

    pygame.display.flip()

pygame.display.quit()
pygame.quit()
