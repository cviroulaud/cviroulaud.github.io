#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 25 Novembre 2021 18:20
"""
from constantes import *
import tkinter


def afficher(grille: list):
    fenetre = tkinter.Tk()
    fenetre.title("Puissance 4")
    canevas = tkinter.Canvas(fenetre,
                             width=LARGEUR * TAILLE,
                             height=HAUTEUR * TAILLE,
                             bg="#0000FF")
    canevas.pack()
    remplir_grille(canevas, grille)

    col = tkinter.StringVar()
    label = tkinter.Label(text="Choisir une colonne:")
    label.pack()
    name = tkinter.Entry(textvariable=col)
    name.focus_set()
    name.pack()
    button = tkinter.Button(text="Placer", command=get_colonne)
    button.pack()
    fenetre.mainloop()
    return canevas


def get_colonne():
    return 1


def couleur_jeton(jeton: int) -> str:
    if jeton == JAUNE:
        return "#FFFF00"
    elif jeton == ROUGE:
        return "#FF0000"
    else:
        return "#FFFFFF"


def remplir_grille(canevas, grille):
    canevas.delete("all")
    for c in range(LARGEUR):
        for l in range(HAUTEUR):
            canevas.create_oval(
                c*TAILLE+MARGE, l*TAILLE+MARGE,
                (c+1) * TAILLE-MARGE, (l+1)*TAILLE-MARGE,
                fill=couleur_jeton(grille[l][c]))


class Moteur():
    def __init__(self, g: list):
        self.grille = g
        self.colonne = -1
        self.fenetre = tkinter.Tk()
        self.fenetre.title("Puissance 4")
        self.canevas = tkinter.Canvas(self.fenetre,
                                      width=LARGEUR * TAILLE,
                                      height=HAUTEUR * TAILLE,
                                      bg="#0000FF")
        self.canevas.pack()
        self.col = tkinter.StringVar()
        label = tkinter.Label(text="Choisir une colonne:")
        label.pack()
        self.name = tkinter.Entry(textvariable=self.col)
        self.name.focus_set()
        self.name.pack()
        button = tkinter.Button(text="Placer", command=self.up_colonne)
        button.pack()
        self.afficher()
        self.fenetre.mainloop()

    def afficher(self) -> None:
        self.canevas.delete("all")
        for c in range(LARGEUR):
            for l in range(HAUTEUR):
                self.canevas.create_oval(
                    c*TAILLE+MARGE, l*TAILLE+MARGE,
                    (c+1) * TAILLE-MARGE, (l+1)*TAILLE-MARGE,
                    fill=self.couleur_jeton(self.grille[l][c]))
        self.fenetre.after(1000, self.afficher)

    def up_colonne(self) -> int:
        self.colonne = int(self.col.get())

    def get_colonne(self) -> int:
        return self.colonne

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
