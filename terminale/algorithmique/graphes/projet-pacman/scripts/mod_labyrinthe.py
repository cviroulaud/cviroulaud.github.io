#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov  9 16:51:50 2020

@auteur: Christophe Viroulaud
"""

from mod_structures import File, Pile
from random import randint, random
import matplotlib.pyplot as plt

class Cellule:
    """
    définit une cellule du labyrinthe
    direction représente les murs ouverts (True) ou non (False)
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.direction = [False] * 4 # N E S O
        self.visite = False

class Labyrinthe:

    def __init__(self, l: int, c: int):
        """
        initialise un tableau de l lignes et c colonnes
        remplit de Cellule() (fermées dans les 4 directions)
        """
        self.lignes = l
        self.colonnes = c
        self.tab = [[Cellule(i, j) for j in range(self.colonnes)] for i in range(self.lignes)]

    def generer(self)->None:
        delta = ((-1,0), (1,0), (0,-1), (0,1))
        # choix d'une cellule de départ
        depart = self.tab[randint(0, self.colonnes-1)][randint(0, self.lignes-1)]
        # parcours en largeur (dans les 4 directions) pour ouvrir ou non les murs
        f = File()
        f.enfiler(depart)
        while not(f.est_vide()):
            en_cours = f.defiler()
            if not(en_cours.visite):
                en_cours.visite = True
                for delta_x, delta_y in delta:
                    # la cellule voisine est-elle dans le tableau?
                    if (en_cours.x + delta_x >= 0) and \
                    (en_cours.x + delta_x < self.colonnes) and \
                    (en_cours.y + delta_y >= 0) and \
                    (en_cours.y + delta_y < self.lignes):
                        voisin = self.tab[en_cours.y+delta_y][en_cours.x+delta_x]
                        # si oui on l'ajoute dans la file
                        f.enfiler(voisin)
                        # on perce certains murs de en_cours et les voisins correspondants
                        for i in range(4):
                            # s'il n'est pas déjà percé
                            if not(en_cours.direction[i]):
                                if random() > 0.85: # chance de percer
                                    en_cours.direction[i] = True
                                    # on perce le mur de voisin correspondant
                                    # ex: S pour N
                                    voisin.direction[(i+2)%4] = True
    def generer2(self)->None:
        delta = ((0,1), (1,0), (0,-1), (-1,0))
        # choix d'une cellule de départ
        depart = self.tab[randint(0, self.colonnes-1)][randint(0, self.lignes-1)]
        # parcours en largeur (dans les 4 directions) pour ouvrir ou non les murs
        p = Pile()
        p.empiler(depart)
        while not(p.est_vide()):
            en_cours = p.depiler()
            if not(en_cours.visite):
                en_cours.visite = True
                voisins = []
                choix_delta = 0
                for delta_x, delta_y in delta:
                    # la cellule voisine est-elle dans le tableau et non visitée?
                    if (en_cours.x + delta_x >= 0) and \
                    (en_cours.x + delta_x < self.colonnes) and \
                    (en_cours.y + delta_y >= 0) and \
                    (en_cours.y + delta_y < self.lignes) and \
                        not(self.tab[en_cours.y+delta_y][en_cours.x+delta_x].visite):
                        # si oui on la garde
                        voisins.append(self.tab[en_cours.y+delta_y][en_cours.x+delta_x])

                    if len(voisins) > 1:
                        voisin = voisins[randint(0, len(voisins)-1)]
                        p.empiler(voisin)
                        en_cours.direction[choix_delta] = True
                        # on perce le mur de voisin correspondant
                        # ex: S pour N
                        voisin.direction[(choix_delta+2)%4] = True

                    choix_delta += 1
            ouvertes = 0
            for porte in en_cours.direction:
                if porte:
                    ouvertes += 1
            if ouvertes < 2:
                p.empiler(en_cours)

    def afficher(self):
        plt.plot([0, 0, self.colonnes, self.colonnes, 0], [0, self.lignes, self.lignes, 0, 0], linewidth=2)
        for i in range(self.colonnes-1):
            for j in range(self.lignes):
                if not (self.tab[i][j].direction[1]):
                    plt.plot([i+1, i+1], [j, j+1], 'b')

        for j in range(self.lignes-1):
            for i in range(self.colonnes):
                if not(self.tab[i][j].direction[0]):
                    plt.plot([i, i+1], [j+1, j+1], 'b')
        plt.axis([-1, self.colonnes+1, -1, self.lignes+1])
        plt.show()

l = Labyrinthe(10,10)
l.generer2()
l.afficher()