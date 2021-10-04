#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 02 Octobre 2021 21:35
"""

VIDE, HOMME, IA = 0, 1, 2


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


def evaluation(grille: list, joueur: int, prof: int) -> int:
    """
    vérifie s'il y a un gagnant

    Args:
        grille (list): plateau
        joueur (int): dernier joueur a avoir placé un pion

    Returns:
        int: score (10 ou -10) ou 0 si pas de gagnant
    """
    # horizontal
    for i in range(3):
        if grille[i][0] != VIDE:
            col = 0
            while col < 3 and grille[i][col] == grille[i][0]:
                col += 1
            if col == 3:  # un gagnant
                if grille[i][0] == IA:
                    return 10-prof
                else:
                    return -10+prof
    # vertical
    for j in range(3):
        if grille[0][j] != VIDE:
            lig = 0
            while lig < 3 and grille[lig][j] == grille[0][j]:
                lig += 1
            if lig == 3:  # un gagnant
                if grille[0][j] == IA:
                    return 10-prof
                else:
                    return -10+prof

    # diagonal (cas où on a placé le pion central)
    # haut-gauche vers bas-droite
    if grille[0][0] != VIDE:
        coord = 0
        while coord < 3 and grille[coord][coord] == grille[0][0]:
            coord += 1
        if coord == 3:  # un gagnant
            if grille[0][0] == IA:
                return 10-prof
            else:
                return -10+prof
    # haut-droite vers bas-gauche
    if grille[0][2] != VIDE:
        l, c = 0, 2
        while c >= 0 and grille[l][c] == grille[0][2]:
            l += 1
            c -= 1
        if c == -1:  # un gagnant
            if grille[0][2] == IA:
                return 10-prof
            else:
                return -10+prof
    # pas de gagnant --> joueur suivant
    return 0


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

c=0
def minmax(grille: list, joueur: int, prof: int, a: int, b: int) -> int:
    global c
    c+=1
    score = evaluation(grille, en_cours, prof)
    if score != 0:  # il y a un gagnant
        return score
    elif est_nul(grille):  # match nul
        return 0

    """
    si on veut s'arrêter à une certaine prof
    if prof == P_MAX:
        eval_score
    """

    if joueur == HOMME:  # min
        mini = 1001
        for i in range(3):
            for j in range(3):
                if grille[i][j] == VIDE:
                    grille[i][j] = HOMME
                    min_enc = minmax(grille, IA, prof+1, a, b)
                    grille[i][j] = VIDE
                    if min_enc < mini:
                        mini = min_enc
                    # coupure alpha
                    if a >= mini:
                        return mini
                    b = min(b, mini) # recalcule beta
        return mini
    else:  # max
        maxi = -1001
        for i in range(3):
            for j in range(3):
                if grille[i][j] == VIDE:
                    grille[i][j] = IA
                    max_enc = minmax(grille, HOMME, prof+1, a, b)
                    grille[i][j] = VIDE
                    if max_enc > maxi:
                        maxi = max_enc
                    # coupure beta
                    if b <= maxi:
                        return maxi
                    a = max(a, maxi) # recalcule alpha
        return maxi


def choix_ia(grille: list) -> tuple:
    maxi = -1001
    mvt = (-1, -1)
    for i in range(3):
        for j in range(3):
            if grille[i][j] == VIDE:
                # place
                grille[i][j] = IA
                max_enc = minmax(grille, HOMME, 0, -1001, 1001)
                # reinit
                grille[i][j] = VIDE
                # garde meilleur mvt
                if max_enc > maxi:
                    maxi = max_enc
                    mvt = (i, j)
    return mvt


grille = [[VIDE for _ in range(3)] for _ in range(3)]

gagnant = False
en_cours = IA

while not gagnant:
    if en_cours == HOMME:
        ligne, colonne = choix_homme(grille)
    else:
        ligne, colonne = choix_ia(grille)
        print(c)
        c=0
    grille[ligne][colonne] = en_cours

    score = evaluation(grille, en_cours, 0)
    if score != 0:  # il y a un gagnant
        gagnant = True
        print(f"Le joueur {en_cours} a gagné.")
    elif est_nul(grille):
        gagnant = True
        print("Match nul")
    else:
        en_cours = en_cours % 2 + 1
    affichage(grille)
