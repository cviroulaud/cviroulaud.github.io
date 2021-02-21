#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 16 15:10:02 2020

@auteur: Christophe Viroulaud
"""


from tkinter import *
from tkinter import ttk
from mod_vie import *
from random import randint

TAILLE = 8
CELLULES = 200
STOP = ""

def compter_voisins(g: list, cel: tuple)->int:
    nb = 0
    delta = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    for decalage in delta:
        ligne, colonne = cel[0]+decalage[0], cel[1]+decalage[1]
        if ligne >= 0 and ligne < CELLULES and colonne >= 0 and colonne < CELLULES:
            if g[ligne][colonne]:
                nb += 1
    return nb

def cycle(f, c, g: list)->None:
    global STOP
    nouvelle = [[False for _ in range(CELLULES)] for _ in range(CELLULES)]

    for i in range(CELLULES):
        for j in range(CELLULES):
            nb_voisins = compter_voisins(g, (i, j))

            if not g[i][j]: # une cellule morte
                if nb_voisins == 3: # devient vivante
                    nouvelle[i][j] = True
            else: # une cellule vivante
                if nb_voisins == 2 or nb_voisins == 3: # le reste
                    nouvelle[i][j] = True

    # la grille est actualisée
    g = nouvelle

    # affichage de la grille
    c.delete("all")
    for i in range(CELLULES):
        for j in range(CELLULES):
            if g[i][j]:
                c.create_oval(TAILLE*(j),
                                    TAILLE*(i),
                                    TAILLE*(j+1),
                                    TAILLE*(i+1),
                                    fill="blue")

    # nouveau cycle
    STOP = f.after(100, cycle, f, c, g)

def nouveau(event):
    """
    choisir un nouveau visuel
    (que en globale...)
    """
    fenetre.after_cancel(STOP)
    grille = [[False for _ in range(CELLULES)] for _ in range(CELLULES)]

    choix = [aleatoire, une_ligne, escalier, vaisseau, vaisseau, canon]
	# Obtenir l'élément sélectionné
    select = listeCombo.current()
    if select == 0:
        choix[select](grille,3000)
    elif select == 1:
        choix[select](grille)
    elif select == 2:
        choix[select](grille)
    elif select == 3:
        choix[select](grille,0)
    elif select == 4:
        for i in range(20):
            choix[select](grille, 10*i)
    elif select == 5:
        choix[select](grille)

    cycle(fenetre, canevas, grille)


"""
programme principal
initialisation de la fenêtre graphique
"""
fenetre = Tk()
fenetre.title("Jeu de la vie")
canevas = Canvas(fenetre, width = CELLULES*TAILLE, height = CELLULES*TAILLE)
canevas.pack()

# choix du visuel
depart=["Aléatoire", "Ligne simple", "Escalier", "Vaisseau","Armée","Canon"]
listeCombo = ttk.Combobox(fenetre, font="Verdana 32", values=depart)
listeCombo.current(0)
listeCombo.pack()
listeCombo.bind("<<ComboboxSelected>>", nouveau)

"""
initialisation de l'état de départ
"""
grille = [[False for _ in range(CELLULES)] for _ in range(CELLULES)]

une_ligne(grille)

cycle(fenetre, canevas, grille)

fenetre.mainloop()
