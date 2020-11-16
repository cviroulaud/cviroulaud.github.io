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
        self.tab = [[Cellule(j, i) for j in range(self.colonnes)] for i in range(self.lignes)]
        self.generer()

    def get_voisins(self, en_cours: object, deja_visite: bool)->set:
        """
        renvoie les voisins non visités de en_cours
        """
        delta = ((-1,0), (1,0), (0,-1), (0,1))
        v = set()
        for delta_x, delta_y in delta:
            # la cellule voisine est-elle dans les limites?
            if (en_cours.x + delta_x >= 0) and \
            (en_cours.x + delta_x < self.colonnes) and \
            (en_cours.y + delta_y >= 0) and \
            (en_cours.y + delta_y < self.lignes):
                voisin = self.tab[en_cours.y+delta_y][en_cours.x+delta_x]
                # on veut les visités ou non
                if voisin.visite == deja_visite:
                    v.add(voisin)
        return v

    def ouvre_mur(self, cel1, cel2, mur):
        cel1.direction[mur] = True
        cel2.direction[(mur+2)%4] = True

    def generer(self)->None:
        # choix d'une cellule de départ
        en_cours = self.tab[randint(0, self.lignes-1)][randint(0, self.colonnes-1)]
        frontieres = {en_cours}
        #frontieres.add(en_cours)
        while len(frontieres) > 0:
            en_cours.visite = True

            # ajout de tous les voisins non visités
            frontieres |= self.get_voisins(en_cours, False)

            # choix d'un voisin
            en_cours = frontieres.pop()

            # récupère un voisin de en_cours qui est déjà dans le labyrinthe
            voisins = self.get_voisins(en_cours, True)
            voisin = voisins.pop()

            # cherche la face commune à en_cours et voisin
            if en_cours.x == voisin.x: # N ou S
                if en_cours.y > voisin.y: # S de en_cours
                    self.ouvre_mur(en_cours, voisin, 2)
                else: # N de en_cours
                    self.ouvre_mur(en_cours, voisin, 0)
            else:
                if en_cours.x > voisin.x: # O de en_cours
                    self.ouvre_mur(en_cours, voisin, 3)
                else: # E de en_cours
                    self.ouvre_mur(en_cours, voisin, 1)

    def afficher(self):
        plt.plot([0, 0, self.colonnes, self.colonnes, 0], [0, self.lignes, self.lignes, 0, 0], linewidth=2)
        for i in range(self.colonnes-1):
            for j in range(self.lignes):
                if not (self.tab[j][i].direction[1]):
                    plt.plot([i+1, i+1], [j, j+1], 'b')

        for j in range(self.lignes-1):
            for i in range(self.colonnes):
                if not(self.tab[j][i].direction[0]):
                    plt.plot([i, i+1], [j+1, j+1], 'b')

        plt.axis('off')
        plt.show()

l = Labyrinthe(20, 20)
l.afficher()