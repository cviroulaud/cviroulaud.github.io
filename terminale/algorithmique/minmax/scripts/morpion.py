#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Oct 15 13:15:18 2020

@auteur: Christophe Viroulaud
"""

"""
initialisation
"""
grille = [[0 for _ in range(3)] for _ in range(3)]

gagnant = False
joueur = 1

while not gagnant:
    """
    le joueur indique les coordonnées de son placement
    exemple: 1 2
    indique la ligne 1 et la colonne 2 en partant du haut gauche
    et en considérant que le joueur compte en partant de 1 et non
    de 0 comme dans la liste
    """
    position_libre = False
    while not position_libre:
        ligne, colonne = map(int, input(f"Joueur {joueur}, entrez les coordonnées (exemple: 3 3): ").split())
        ligne -= 1
        colonne -= 1
        if grille[ligne][colonne] == 0:
            grille[ligne][colonne] = joueur
            position_libre = True
        else:
            print("La position n'est pas libre.")

    """
    vérification de l'alignement:
    """
    #horizontal
    total = 0
    for i in range(3):
        if grille[ligne][i] == joueur:
            total += 1
    if total == 3:
        gagnant = True
    else:
        #vertical
        total = 0
        for i in range(3):
            if grille[i][colonne] == joueur:
                total += 1
        if total == 3:
            gagnant = True
        else:
            #diagonal (cas où on a placé le pion central)
            #haut vers bas
            total = 0
            for i in range(3):
                if grille[i][i] == joueur:
                    total += 1
            if total == 3:
                gagnant = True
            else:
                #cas bas vers haut
                total = 0
                for i in range(3):
                    if grille[2-i][i] == joueur:
                        total += 1
                if total == 3:
                    gagnant = True
                else:
                    #pas de gagnant, joueur suivant
                    if joueur == 1:
                        joueur = 2
                    else:
                        joueur = 1
    """
    affichage grille
    """
    for i in range(3):
        for j in range(3):
            if grille[i][j] == 0:
                print(" ",end="")
            elif grille[i][j] == 1:
                print("X",end="")
            else:
                print("O",end="")

            if j < 2:
                print(" | ",end="")
            else:
                print()
        if i < 2:
            print("----------")


print(f"Le joueur {joueur} a gagné.")