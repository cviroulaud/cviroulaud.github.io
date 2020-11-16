#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov  9 16:51:50 2020

@auteur: Christophe Viroulaud
"""

from mod_structures import File, Pile
from random import randint, random
import pygame
from constantes import *


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
        self.piece = False

class Labyrinthe:

    def __init__(self, f):
        """
        initialise un tableau de 'hauteur' lignes et 'largeur' colonnes
        remplit de Cellule() (fermées dans les 4 directions)
        """
        self.fenetre = f
        self.lignes = hauteur
        self.colonnes = largeur
        self.fond = pygame.image.load(img_fond).convert()
        self.fond = pygame.transform.scale(self.fond, (largeur*taille, hauteur*taille))
        self.tab = [[Cellule(j, i) for j in range(self.colonnes)] for i in range(self.lignes)]
        self.mur_h = pygame.image.load(img_mur)
        self.mur_h = pygame.transform.scale(self.mur_h, (taille, taille//10))
        self.mur_v = pygame.image.load(img_mur)
        self.mur_v = pygame.transform.rotate(self.mur_v, 90)
        self.mur_v = pygame.transform.scale(self.mur_v, (taille//10, taille))
        self.piece = pygame.image.load(img_piece)
        self.piece = pygame.transform.scale(self.piece, (taille, taille))

        self.coord_pieces = set()

        self.generer()
        self.placer_pieces(10)

    def get_voisins(self, en_cours: object, deja_visite: bool)->set:
        """
        renvoie les voisins de en_cours

        Parameters
        ----------
        en_cours : object
            la cellule en cours.
        deja_visite : bool
            si True renvoie les cellules déjà dans le labyrinthe
            si False renvoie les cellules frontière

        Returns
        -------
        set
            les voisins de en_cours.

        """
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
        """
        crée le labyrinthe (Algorithme de Prim):
            choisis une cellule et la marque (est dans le labyrinthe)
            récupère les voisines (frontières du labyrinthe)
            choisis une de ces voisines
            ouvre le mur entre le labyrinthe et cette cellule
            recommence
        """
        # choix d'une cellule de départ
        en_cours = self.tab[randint(0, self.lignes-1)][randint(0, self.colonnes-1)]
        frontieres = set()
        # initialise à 1 car pour la dernière cellule,
        # le compteur n'est pas incrémenté
        nb_visites = 1

        while not(nb_visites == nb_cel):
            en_cours.visite = True
            nb_visites += 1

            # ajout de tous les voisins non visités
            frontieres |= self.get_voisins(en_cours, False)

            # choix d'un voisin
            en_cours = frontieres.pop()

            # récupère un voisin de en_cours qui est déjà dans le labyrinthe
            voisins = self.get_voisins(en_cours, True)
            voisin = voisins.pop()

            # cherche la face commune à en_cours et voisin
            if en_cours.x == voisin.x: # N ou S
                if en_cours.y > voisin.y: # N de en_cours
                    self.ouvre_mur(en_cours, voisin, 0)
                else: # S de en_cours
                    self.ouvre_mur(en_cours, voisin, 2)
            else:
                if en_cours.x > voisin.x: # O de en_cours
                    self.ouvre_mur(en_cours, voisin, 3)
                else: # E de en_cours
                    self.ouvre_mur(en_cours, voisin, 1)

    def placer_pieces(self, n: int):
        """
        place n pièces dans le labyrinthe
        """
        nb_places = 0
        while nb_places < n:
            x = randint(0, self.colonnes-1)
            y = randint(0, self.lignes-1)
            if not(self.tab[x][y].piece):
                self.tab[x][y].piece = True
                # enregistre les coordonnées
                self.coord_pieces.add((x,y))
                nb_places += 1

    def afficher(self):
        """
        affiche le labyrinthe
        du fait de la redondance, crée les murs S et E seulement
        """
        self.fenetre.blit(self.fond, (0,0))

        # contour
        offset = taille//10
        for i in range(self.colonnes):
            self.fenetre.blit(self.mur_h, (i*taille,0))
            self.fenetre.blit(self.mur_h, (i*taille, self.lignes * taille-offset))

        for j in range(self.lignes):
            self.fenetre.blit(self.mur_v, (0, j*taille))
            self.fenetre.blit(self.mur_v, (self.colonnes * taille-offset, j*taille))

        # murs E
        for i in range(self.colonnes-1):
            for j in range(self.lignes):
                if not(self.tab[j][i].direction[1]):
                    self.fenetre.blit(self.mur_v, ((i+1)*taille,j*taille))

        # murs S
        for j in range(self.lignes-1):
            for i in range(self.colonnes):
                if not(self.tab[j][i].direction[2]):
                    self.fenetre.blit(self.mur_h, (i*taille,(j+1)*taille))

        # placement des pièces
        for i in range(self.colonnes):
            for j in range(self.lignes):
                if self.tab[j][i].piece:
                    self.fenetre.blit(self.piece, (i*taille, j*taille))

if __name__ == "__main__":
    l = Labyrinthe(20, 20)
    l.afficher()