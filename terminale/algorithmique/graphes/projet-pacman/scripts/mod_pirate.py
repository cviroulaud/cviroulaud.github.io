#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 16 09:13:09 2020

@auteur: Christophe Viroulaud
"""


import pygame
from constantes import *

class Pirate:
    def __init__(self, f):
        self.fenetre = f
        self.lignes = hauteur
        self.colonnes = largeur
        self.pirate = pygame.image.load(img_pirate).convert_alpha()
        self.pirate = pygame.transform.scale(self.pirate, (taille, taille))
        self.x = 0
        self.y = 0

    def deplacer(self, dpct: int, tab: object):
        """
        modifie la position du pirate

        Parameters
        ----------
        dpct : int
            direction N: 0, E: 1, S:2, 0:3.
        tab : object
            le labyrinthe.
        """
        if tab[self.x][self.y].direction[dpct]:
            self.x += delta[dpct][1]
            self.y += delta[dpct][0]

    def afficher(self):
        """
        affiche le pirate
        """
        self.fenetre.blit(self.pirate, (self.x*taille, self.y*taille))
