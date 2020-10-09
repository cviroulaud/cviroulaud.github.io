#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct  9 11:50:25 2020

@auteur: Christophe Viroulaud
"""


import tkinter as tk


"""
def deplacement_pion_2(event,t):
    pass
def boucle_jeu():

    plateau.after(1000,boucle_jeu)
"""

def choix_position(event):
    if event.keysym == "Right" and plateau.coords(nouveau_pion)[0] < TAILLE*6:
        plateau.move(nouveau_pion, TAILLE, 0)
    if event.keysym == "Left" and plateau.coords(nouveau_pion)[0] > TAILLE:
        plateau.move(nouveau_pion, -TAILLE, 0)
    if event.keysym == "space":
        positionnement_pion()

def positionnement_pion():
    colonne = plateau.coords(nouveau_pion)[0] // TAILLE
    print(colonne)

"""
paramétrage de la fenêtre
"""
TAILLE = 200
GAGNE = False
racine = tk.Tk()
plateau = tk.Canvas(racine, width=TAILLE*7, height=TAILLE*7, bg="white")
plateau.pack()

"""
grille de jeu
0 = vide
1 = rouge
2 = jaune
"""
grille = [[0 for i in range(7)] for j in range(6)]
"""
création graphique de la grille
"""
plateau.create_rectangle(0,TAILLE,TAILLE*7,TAILLE*7, fill='blue')
for i in range(7):
    for j in range(6):
        plateau.create_oval(TAILLE*(i+0.1),
                            TAILLE*(j+1.1),#ajout de 1 pour bande blanche en haut
                            TAILLE*(i+0.9),
                            TAILLE*(j+1.9),#ajout de 1 pour bande blanche en haut
                            fill='white')

"""
gestion des touches
"""
#racine.bind("<Key>", lambda e: deplacement_pion(e,"test"))
racine.bind("<Key>", choix_position)

"""
pion à placer
"""
tour = 1
if not GAGNE:
    if tour == 1:
        couleur = "red"
    else:
        couleur = "yellow"
        nouveau_pion = plateau.create_oval(TAILLE*0.1,
                                           TAILLE*0.1,
                                           TAILLE*0.9,
                                           TAILLE*0.9,
                                           fill=couleur)

racine.mainloop()