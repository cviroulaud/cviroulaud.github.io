#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov  9 16:51:50 2020

@auteur: Christophe Viroulaud
"""

import pygame
from constantes import *


class Cellule:
    """
    définit une cellule du labyrinthe
    direction représente les murs ouverts (True) ou non (False)
    """

    def __init__(self):
        self.direction = [False] * 4  # N E S O
        self.visite = False


class Labyrinthe:

    def __init__(self, f):
        """
        initialise un tableau de 'hauteur' lignes et 'largeur' colonnes
        remplit de Cellule() (fermées dans les 4 directions)
        """
        self.fenetre = f
        self.lignes = hauteur
        self.colonnes = largeur
        self.laby = [[Cellule() for i in range(self.colonnes)]
                     for j in range(self.lignes)]
        self.creer()

    def creer(self) -> None:
        """
        crée les murs
        """
        # bords horizontaux
        for x in range(self.colonnes):
            self.laby[0][x].direction[0] = True
            self.laby[self.lignes-1][x].direction[2] = True

        # bords verticaux
        for y in range(self.lignes):
            self.laby[y][0].direction[3] = True
            self.laby[y][self.colonnes-1].direction[1] = True

        # murs
        for y in range(6, 15):
            self.laby[y][16].direction[1] = True
        for x in range(5, 17):
            self.laby[14][x].direction[2] = True

    def afficher_cellules(self):
        # carreaux
        for y in range(self.lignes):
            for x in range(self.colonnes):
                pygame.draw.rect(
                    self.fenetre, BLACK, (x*taille+bordure, y*taille+bordure, taille, taille), 1)

                if self.laby[y][x].visite:
                    pygame.draw.rect(
                        self.fenetre, PURPLE, (x*taille+bordure+1, y*taille+bordure+1, taille-2, taille-2))

    def afficher_murs(self):
        """
        du fait de la redondance, crée les murs S et E seulement
        """
        # contour N O
        for i in range(self.colonnes):
            pygame.draw.line(self.fenetre, BLACK, (i*taille+bordure,
                             bordure), ((i+1)*taille+bordure, bordure), bordure)

        for j in range(self.lignes):
            pygame.draw.line(self.fenetre, BLACK, (bordure, j *
                             taille+bordure), (bordure, (j+1)*taille+bordure), bordure)

        # murs
        for y in range(self.lignes):
            for x in range(self.colonnes):
                # mur E
                if self.laby[y][x].direction[1]:
                    pygame.draw.line(self.fenetre, BLACK, ((
                        x+1)*taille+bordure, y*taille+bordure), ((x+1)*taille+bordure, (y+1)*taille+bordure), bordure)
                # mur S
                if self.laby[y][x].direction[2]:
                    pygame.draw.line(self.fenetre, BLACK, (x*taille+bordure, (y+1)*taille +
                                     bordure), ((x+1)*taille+bordure, (y+1)*taille+bordure), bordure)
