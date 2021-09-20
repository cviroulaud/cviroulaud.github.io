#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 20 Septembre 2021 08:09
"""

import tkinter as tk
REINES = 8
TAILLE = 50


def reines():
    def placer_reine(res: list, ligne: int):
        """
        Args:
            res (list): indice = ligne, élément = colonne
            ligne (int): ligne en cours de remplissage

        Returns:
            [type]: res
        """
        if ligne == REINES:  # fin du plateau
            return True
        else:
            for col in range(REINES):  # teste chaque colonne
                possible = True
                for k in range(ligne):  # chaque ligne précédante
                    # teste même col et les 2 diago (x+y=x'+y' ou x-=x'-y')
                    if res[k] == col or res[k]+k == col+ligne or res[k]-k == col-ligne:
                        possible = False
                        break  # avec un while...

                if possible:
                    res[ligne] = col  # on place la reine
                    if placer_reine(res, ligne+1):  # ligne suivante
                        return True
            return False                    
            """
            si on a testé toutes les colonnes de la ligne
            on sort de la boucle et on revient (récursif) à la ligne préc (backtracking)
            """

    r = [-1 for _ in range(REINES)]
    placer_reine(r, 0)
    return r


placements = reines()

fen = tk.Tk()
can = tk.Canvas(fen, width=TAILLE*REINES, height=TAILLE*REINES)
can.pack()

for i in range(1, REINES):
    # lignes verticales
    can.create_line(TAILLE*i, 0, TAILLE*i, TAILLE*REINES)
    # lignes horizontales
    can.create_line(0, TAILLE*i, TAILLE*REINES, TAILLE*i)

for i in range(REINES):
    can.create_oval(placements[i]*TAILLE,
                    i*TAILLE,
                    (placements[i]+1)*TAILLE,
                    (i+1)*TAILLE,
                    fill="#FF0000")
fen.mainloop()
