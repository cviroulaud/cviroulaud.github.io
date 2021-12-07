#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 25 Novembre 2021 18:20
"""
from constantes import *
import tkinter


class Moteur:
    def __init__(self):
        self.fenetre = tkinter.Tk()
        self.fenetre.title("Puissance 4")
        self.canevas = tkinter.Canvas(self.fenetre,
                                      width=LARGEUR * TAILLE,
                                      height=HAUTEUR * TAILLE,
                                      bg="#0000FF")
        self.canevas.pack()

    def afficher(self, grille: list) -> None:
        self.fenetre.update_idletasks()
        self.fenetre.update()
        for c in range(LARGEUR):
            for l in range(HAUTEUR):
                self.canevas.create_oval(
                    c*TAILLE+MARGE, l*TAILLE+MARGE,
                    (c+1) * TAILLE-MARGE, (l+1)*TAILLE-MARGE,
                    fill=self.couleur_jeton(grille[l][c]))

    def afficher_fin(self, grille: list) -> None:
        self.afficher(grille)
        self.fenetre.mainloop()

    def couleur_jeton(self, jeton: int) -> str:
        if jeton == JAUNE:
            return "#FFFF00"
        elif jeton == ROUGE:
            return "#FF0000"
        else:
            return "#FFFFFF"


if __name__ == "__main__":
    moteur = Moteur()
