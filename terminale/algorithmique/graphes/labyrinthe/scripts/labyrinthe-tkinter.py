#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 13 Mars 2022 22:44
"""

import tkinter
from constantes import *
from joueur import Joueur


def jeu():
    canevas.delete("all")
    # grille
    for i in range(TAILLE):
        canevas.create_line(i*DIM, 0, i*DIM, TAILLE*DIM, fill="black", width=2)
        canevas.create_line(0, i*DIM, TAILLE*DIM, i *
                            DIM,  fill="black", width=2)

    # cercle bleu
    canevas.create_oval(joueur.ligne*DIM,
                        joueur.colonne*DIM,
                        (joueur.ligne+1) * DIM,
                        (joueur.colonne+1)*DIM,
                        fill="blue")

    # répétition de la boucle
    fenetre.after(100, jeu)


# fenêtre d'affichage
fenetre = tkinter.Tk()
fenetre.title("Dessiner")
canevas = tkinter.Canvas(fenetre,
                         width=DIM * TAILLE,
                         height=DIM * TAILLE,
                         bg="#FFFFFF")
canevas.pack()

# création d'un cercle déplaçable
joueur = Joueur()
# écoutes
fenetre.bind("<Right>", joueur.deplacement)
fenetre.bind("<Left>", joueur.deplacement)

# boucle de jeu
jeu()
fenetre.mainloop()
