#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct  9 11:50:25 2020

@auteur: Christophe Viroulaud
"""


import tkinter as tk

def choix_position(event):
    """


    Parameters
    ----------
    event : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    global pion,joueur
    if event.keysym == "Right" and plateau.coords(pion)[0] < TAILLE*6:
        plateau.move(pion, TAILLE, 0)
    if event.keysym == "Left" and plateau.coords(pion)[0] > TAILLE:
        plateau.move(pion, -TAILLE, 0)
    if event.keysym == "space":
        x = int(plateau.coords(pion)[0] // TAILLE)
        y = 0
        while y < 6 and grille[y][x] == VIDE:
            y += 1
        #si la colonne n'est pas pleine
        if y-1 >= 0:
            grille[y-1][x] = joueur
            creer_pion(joueur, y, x)
            if not verif_gagnant(joueur, y-1, x): #nouveau tour
                joueur = (joueur+1)%2
                pion = creer_pion(joueur)
            else: #gagné
                plateau.create_text(TAILLE*7//2, TAILLE//2,
                                     text="GAGNÉ",
                                     font="Arial 36")
                plateau.unbind("<Right>")
                plateau.unbind("<Left>")
                plateau.unbind("<space>")



def selection_cases(ligne: int, colonne: int, pas_ligne: int, pas_colonne: int)->list:
    """
    renvoie un tableau de 7 éléments maximum (3 avant et 3 après le pion juste placé)

    Paramètres
    -----
    ligne : int
        la ligne du pion juste placé
    colonne : int
        la colonne du pion juste placé
    pas_ligne : int
        la direction de progression (-1, 0 ou 1)
    pas_colonne : int
        la direction de progression (0 ou 1)

    Renvoie
    -----
    tableau de 7 éléments maximum
    """
    res = []
    #reculer vers les positions de départ
    dep_ligne = ligne - 3*pas_ligne
    if dep_ligne < 0:
        dep_ligne = 0

    dep_colonne = colonne - 3*pas_colonne
    if dep_colonne < 0:
        dep_colonne = 0

    #construction de la liste des cases
    i = 0
    while i < 7 and dep_ligne < 6 and dep_colonne < 7:
        res.append(grille[dep_ligne][dep_colonne])
        dep_ligne += pas_ligne
        dep_colonne += pas_colonne
        i += 1

    return res

def a_4_alignes(tab: list, joueur: int)->bool:
    """
    Renvoie True si le joueur a gagné

    Paramètres
    ----------
    tab : list
        le tableau des cases à vérifier.
    joueur : int
        le numéro du joueur.

    Returns
    -------
    bool
    """
    if len(tab) < 4:
        return False

    nb_alignes = 0
    for e in tab:
        if e == joueur:
            nb_alignes += 1
        else:
            nb_alignes == 0

    return nb_alignes == 4

def verif_gagnant(joueur: int, ligne: int, colonne: int)->bool:
    """
    vérifie si le joueur qui vient de poser un pion est gagnant

    Paramètres
    ----------
    joueur : int
        le joueur qui vient de oser un pion.
    ligne : int
        ligne jouée.
    colonne : int
        colonne jouée.

    Returns
    -------
    bool
        True si gagnant, False sinon.
    """
    #vertical
    if a_4_alignes(selection_cases(ligne, colonne, 1, 0), joueur):
        return True
    #horizontal
    elif a_4_alignes(selection_cases(ligne, colonne, 0, 1), joueur):
        return True
    #diagonal bas vers haut
    elif a_4_alignes(selection_cases(ligne, colonne, 1, 1), joueur):
        return True
    #diagonal haut vers bas
    elif a_4_alignes(selection_cases(ligne, colonne, -1, 1), joueur):
        return True
    else:
        return False

def creer_pion(joueur: int, ligne: int = 0, colonne: int = 0):
    """


    Parameters
    ----------
    joueur : int
        DESCRIPTION.
    ligne : int, optional
        DESCRIPTION. The default is 0.
    colonne : int, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if joueur == ROUGE:
        couleur = "red"
    else:
        couleur = "yellow"

    try:
        plateau.delete(pion)
    except NameError:
        pass

    return plateau.create_oval(TAILLE*(colonne+0.1),
                        TAILLE*(ligne+0.1),
                        TAILLE*(colonne+0.9),
                        TAILLE*(ligne+0.9),
                        fill=couleur)

"""
paramétrage de la fenêtre
"""
TAILLE = 200
VIDE = -1
ROUGE = 0
JAUNE = 1
racine = tk.Tk()
plateau = tk.Canvas(racine, width=TAILLE*7, height=TAILLE*7, bg="white")
plateau.pack()

grille = [[VIDE for i in range(7)] for j in range(6)]
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
1° pion à placer
"""
joueur = ROUGE
pion = creer_pion(joueur)

"""
gestion des touches
"""
racine.bind("<Key>", choix_position)
#racine.bind("<Key>", lambda event: choix_position(event,joueur,pion,grille))

racine.mainloop()