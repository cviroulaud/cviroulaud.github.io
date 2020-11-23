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
    taille_case = 100

    def __init__(self, taille):
        self.taille = taille
        self.graphe = Graphe(self.taille)
        self.creer_graphe()
        self.remplir_rec()

        self.fenetre = Tk()
        self.fenetre.title('Sudoku')
        self.canevas = Canvas(self.fenetre,width=Sudoku.taille_case*self.taille,
                                          height=Sudoku.taille_case*self.taille)
        self.canevas.pack()

    def creer_graphe(self):
        """
        Initialise le graphe des cases liées
        """
        # arêtes verticales
        for j in range(self.taille):
            for i in range(self.taille-1):
                for k in range(i+1, self.taille):
                    self.graphe.ajouter_arete((j,i),(j,k))

        # arêtes horizontales
        for i in range(self.taille):
            for j in range(self.taille-1):
                for k in range(j+1, self.taille):
                    self.graphe.ajouter_arete((j,i),(k,i))

        # blocs
        nb_blocs = int(sqrt(self.taille))
        # il y a (nb_blocs*nb_blocs) blocs
        for bloc_lig in range(nb_blocs):
            for bloc_col in range(nb_blocs):
                # pour chaque case
                for i in range(nb_blocs):
                    for j in range(nb_blocs):
                        # vers chaque case
                        for lig in range(nb_blocs):
                            for col in range(nb_blocs):
                                if not((j,i) == (col,lig)):
                                    """
                                    on ne crée pas d'arête vers lui-même
                                    par contre on ne gère pas les éventuels doublons:
                                    l'ensemble (set) dans ajouter_arete le fait pour nous
                                    """
                                    self.graphe.ajouter_arete(
                                        (bloc_col*nb_blocs+j, bloc_lig*nb_blocs+i),
                                        (bloc_col*nb_blocs+col, bloc_lig*nb_blocs+lig)
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
        if y == (self.taille - 1): # dernière colonne
            x += 1
            y = 0
        else:
            y += 1
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
            if choix == self.graphe.get_sommet(v).val:
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
        if s[0] == self.taille:
            return True

        # test des valeurs possibles
        choix = list(range(1,self.taille+1))
        shuffle(choix)
        for val in choix:
            # regarde si choix n'est pas déjà dans les voisins
            if self.est_possible(s, val):
                self.graphe.get_sommet(s).val = val
                if self.remplir_rec(self.case_suivante(s)):
                    return True

        # Tous les chiffres ont été testés et aucun ne fonctionne
        # on réinitialise alors la case
        self.graphe.get_sommet(s).val = 0
        return False

    def afficher(self):
        for l in range(self.taille):
            for c in range(self.taille):
                # ligne verticale
                if c%sqrt(self.taille) == 0:
                    trait_vert = 3
                else:
                    trait_vert = 1

                self.canevas.create_line(Sudoku.taille_case*c,
                                     0,
                                     Sudoku.taille_case*c,
                                     Sudoku.taille_case*self.taille,
                                     width=trait_vert)
                # ligne horizontale
                if l%sqrt(self.taille) == 0:
                    trait_hori = 3
                else:
                    trait_hori = 1
                self.canevas.create_line(0,
                                         Sudoku.taille_case*l,
                                         Sudoku.taille_case*self.taille,
                                         Sudoku.taille_case*l,
                                         width=trait_hori)
                # chiffre
                self.canevas.create_text(Sudoku.taille_case*c + Sudoku.taille_case//2,
                                         Sudoku.taille_case*l + Sudoku.taille_case//2,
                                         text=str(self.graphe.get_sommet((l,c)).val),
                                         font="Arial "+str(Sudoku.taille_case//2))
        self.fenetre.mainloop()

if __name__ == "__main__":
    sudoku = Sudoku(9)
    sudoku.afficher()