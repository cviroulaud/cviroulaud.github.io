#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Oct 15 13:15:18 2020

@auteur: Christophe Viroulaud
"""

from random import choice


def affichage(grille: list) -> None:
    """
    affichage grille
    """
    for i in range(3):
        for j in range(3):
            if grille[i][j] == 0:
                print(" ", end="")
            elif grille[i][j] == 1:
                print("X", end="")
            else:
                print("O", end="")

            if j < 2:
                print(" | ", end="")
            else:
                print()
        if i < 2:
            print("----------")


def est_gagnant(grille: list, joueur: int, coord: tuple) -> bool:
    """
    vérifie si le placement du pion coord
    donne une position gagnante
    """
    ligne = coord[0]
    colonne = coord[1]
    # horizontal
    total = 0
    for i in range(3):
        if grille[ligne][i] == joueur:
            total += 1
    if total == 3:
        return True
    else:
        # vertical
        total = 0
        for i in range(3):
            if grille[i][colonne] == joueur:
                total += 1
        if total == 3:
            return True
        else:
            # diagonal (cas où on a placé le pion central)
            # haut vers bas
            total = 0
            for i in range(3):
                if grille[i][i] == joueur:
                    total += 1
            if total == 3:
                return True
            else:
                # cas bas vers haut
                total = 0
                for i in range(3):
                    if grille[2-i][i] == joueur:
                        total += 1
                if total == 3:
                    return True
                else:
                    # pas de gagnant, joueur suivant
                    return False


def est_nul(grille: list) -> bool:
    """
    vérifie si match nul
    = toutes les cases remplies
    """
    for ligne in range(3):
        for colonne in range(3):
            # s'il y a encore une case vide
            if grille[ligne][colonne] == 0:
                return False
    return True


def minmax(grille: list) -> tuple:
    score_max = -1000
    choix_max = []
    for ligne in range(3):
        for colonne in range(3):
            # si la place est libre
            if grille[ligne][colonne] == 0:
                grille[ligne][colonne] = IA
                score = mini(grille, (ligne, colonne))
                #print(ligne, colonne, score)
                if score > score_max:
                    # réinit les choix
                    score_max = score
                    choix_max = [(ligne, colonne)]
                elif score == score_max:
                    # ajoute nouvelle possibilité
                    choix_max.append((ligne, colonne))

                grille[ligne][colonne] = 0
    return choice(choix_max)


def maxi(grille: list, coord: tuple) -> int:
    """
    évalue le score de l'HOMME si fin du jeu (gagnant ou nul)
    sinon place un pion IA
    """
    if est_gagnant(grille, HOMME, coord):
        return -1000

    if est_nul(grille):
        return 0

    score_max = -1000
    for ligne in range(3):
        for colonne in range(3):
            # si la place est libre
            if grille[ligne][colonne] == 0:
                grille[ligne][colonne] = IA
                score = mini(grille, coord)
                if score > score_max:
                    score_max = score
                grille[ligne][colonne] = 0
    return score_max


def mini(grille: list, coord: tuple) -> int:
    """
    évalue le score de l'IA si fin du jeu (gagnant ou nul)
    sinon place un pion HOMME
    """
    if est_gagnant(grille, IA, coord):
        return 1000

    if est_nul(grille):
        return 0

    score_min = 1000
    for ligne in range(3):
        for colonne in range(3):
            # si la place est libre
            if grille[ligne][colonne] == 0:
                grille[ligne][colonne] = HOMME
                score = maxi(grille, coord)
                if score < score_min:
                    score_min = score
                grille[ligne][colonne] = 0
    return score_min


def choix_homme(grille: list) -> tuple:
    """
    demande la position du pion de l'HOMME
    tant que son choix est mauvais (déjà pris)

    le joueur indique les coordonnées de son placement
    exemple: 1 2
    indique la ligne 1 et la colonne 2 en partant du haut gauche
    et en considérant que le joueur compte en partant de 1 et non
    de 0 comme dans la liste
    """
    position_libre = False
    while not position_libre:
        ligne, colonne = map(int, input(
            f"Entrez les coordonnées (exemple: 3 3): ").split())
        ligne -= 1
        colonne -= 1
        if grille[ligne][colonne] == 0:
            return (ligne, colonne)
        else:
            print("La position n'est pas libre.")


"""
initialisation
"""
grille = [[0 for _ in range(3)] for _ in range(3)]

gagnant = False
HOMME = 1
IA = 2
en_cours = HOMME

while not gagnant:
    if en_cours == HOMME:
        ligne, colonne = choix_homme(grille)
    else:
        ligne, colonne = minmax(grille)
    grille[ligne][colonne] = en_cours
    
    if est_gagnant(grille, en_cours, (ligne, colonne)):
        gagnant = True
        print(f"Le joueur {en_cours} a gagné.")
    elif est_nul(grille):
        gagnant = True
        print("Match nul")
    else:
        en_cours = en_cours % 2 + 1
    affichage(grille)
