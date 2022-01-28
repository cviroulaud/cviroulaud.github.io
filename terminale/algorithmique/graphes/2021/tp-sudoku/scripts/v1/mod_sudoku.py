#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 16 11:20:57 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe
from math import sqrt
from random import shuffle
from structures import Pile
from tkinter import *

class Sudoku:

    def __init__(self, taille):
        self.taille = taille
        self.grille = [[0 for _ in range(self.taille)] for _ in range(self.taille)]
        self.graphe = Graphe()
        self.creer_graphe()
        self.remplir_rec()

    def creer_graphe(self):
        """
        Initialise le graphe des cases liées
        """
        # création des sommets
        for x in range(self.taille):
            for y in range(self.taille):
                self.graphe.ajouter_sommet((x,y))

        # arêtes verticales
        for x in range(self.taille):
            for y in range(self.taille-1):
                for k in range(y+1, self.taille):
                    self.graphe.ajouter_arete((x,y),(x,k))

        # arêtes horizontales
        for y in range(self.taille):
            for x in range(self.taille-1):
                for k in range(x+1, self.taille):
                    self.graphe.ajouter_arete((x,y),(k,y))

        # blocs
        nb_blocs = int(sqrt(self.taille))
        # il y a (nb_blocs*nb_blocs) blocs
        for i in range(nb_blocs):
            for j in range(nb_blocs):
                # pour chaque case
                for y in range(nb_blocs):
                    for x in range(nb_blocs):
                        # vers chaque case
                        for lig in range(nb_blocs):
                            for col in range(nb_blocs):
                                if not((x,y) == (col,lig)):
                                    """
                                    on ne crée pas d'arête vers lui-même
                                    par contre on ne gère pas les éventuels doublons:
                                    l'ensemble (set) dans ajouter_arete le fait pour nous
                                    """
                                    self.graphe.ajouter_arete(
                                        (j*nb_blocs + x  , i*nb_blocs + y),
                                        (j*nb_blocs + col, i*nb_blocs + lig)
                                        )

    def case_suivante(self, s: tuple)->tuple:
        """
        retourne la prochaine case à visiter

        Parameters
        ----------
        s : tuple
            le sommet actuel.

        Returns
        -------
        tuple
            le prochain sommet.
        """
        x,y = s[0],s[1]
        if x == (self.taille - 1): # dernière colonne
            y += 1
            x = 0
        else:
            x += 1
        return (x,y)

    def est_possible(self, s: tuple, choix: int)->bool:
        """
        vérifie si choix n'est pas déjà utilisé

        Parameters
        ----------
        choix : int
            la valeur à tester.

        Returns
        -------
        bool
        """
        for v in self.graphe.get_adjacents(s):
            if choix == self.grille[v[0]][v[1]]:
                return False
        return True

    def remplir_rec(self, s: tuple = (0,0)):
        """
        parcourt la grille de gauhe à droite
        et de haut en bas et la remplit récursivement

        Parameters
        ----------
        s : tuple, optional
            le sommet en cours. The default is (0,0).

        Returns
        -------
        bool
            True si le chiffre est placé.

        """
        # si on a tout rempli = on sort du tableau
        if s[1] == self.taille:
            return True

        # test des valeurs possibles
        chiffres = list(range(1,self.taille+1))
        shuffle(chiffres)
        for val in chiffres:
            # regarde si val n'est pas déjà dans les voisins
            if self.est_possible(s, val):
                self.grille[s[0]][s[1]] = val
                # appelle récursivement la fonction pour la case suivante
                if self.remplir_rec(self.case_suivante(s)):
                    return True

        # Tous les chiffres ont été testés et aucun ne fonctionne
        # on réinitialise alors la case
        self.grille[s[0]][s[1]] = 0
        return False

    def afficher(self):
        taille_case = 100
        self.fenetre = Tk()
        self.fenetre.title('Sudoku')
        self.canevas = Canvas(self.fenetre,width=taille_case*self.taille,
                                          height=taille_case*self.taille)
        self.canevas.pack()

        for l in range(self.taille):
            for c in range(self.taille):
                # ligne verticale
                if c%sqrt(self.taille) == 0:
                    trait_vert = 3
                else:
                    trait_vert = 1

                self.canevas.create_line(taille_case*c,
                                     0,
                                     taille_case*c,
                                     taille_case*self.taille,
                                     width=trait_vert)
                # ligne horizontale
                if l%sqrt(self.taille) == 0:
                    trait_hori = 3
                else:
                    trait_hori = 1
                self.canevas.create_line(0,
                                         taille_case*l,
                                         taille_case*self.taille,
                                         taille_case*l,
                                         width=trait_hori)
                # chiffre
                self.canevas.create_text(taille_case*c + taille_case//2,
                                         taille_case*l + taille_case//2,
                                         text=str(self.grille[l][c]),
                                         font="Arial "+str(taille_case//2))
        self.fenetre.mainloop()

if __name__ == "__main__":
    sudoku = Sudoku(9)
    print(sudoku.grille)
    sudoku.afficher()
