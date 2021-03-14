#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/11 09:14:48
"""

COMPTEUR = 0

def decoupe_naif(l: int, prix: dict)->int:
    """
    renvoie le prix maximum pour une barre de taille l
    """
    global COMPTEUR
    if l == 0:
        return 0
    val_max = 0
    for taille, valeur in prix.items():
        if l >= taille:
            COMPTEUR += 1
            val_max = max(val_max, decoupe_naif(l-taille, prix)+valeur)
    return val_max

longueur = 10
# prix correspondant à chaque taille de découpe
prix = {1: 2, 2: 5, 3: 8, 4: 10, 5: 11, 6: 14, 8: 17, 10: 20}
print(decoupe_naif(longueur, prix))
print(COMPTEUR)

def decoupe_TD(l: int, prix: dict, track: int)->int:
    """
    renvoie le prix maximum pour une barre de taille l
    """
    global COMPTEUR
    if track[l] > 0:
        return track[l]
    if l == 0:
        track[0] = 0
        return track[0]
    val_max = 0
    for taille, valeur in prix.items():
        if l >= taille:
            COMPTEUR += 1
            val_max = max(val_max, decoupe_TD(l-taille, prix, track)+valeur)
    track[l] = val_max
    return track[l]

COMPTEUR = 0
track = [-1 for _ in range(longueur+1)]
print(decoupe_TD(longueur, prix, track))
print(COMPTEUR)

def decoupe_BU(l: int, prix: dict)->int:
    global COMPTEUR
    track = [0 for _ in range(longueur+1)]
    # calcule le prix pour chaque longueur en partant des petites valeurs
    for i in range(1, longueur+1):
        val_max = 0
        for taille, valeur in prix.items():
            if i >= taille:
                COMPTEUR += 1
                val_max = max(val_max, track[i-taille]+valeur)
        track[i] = val_max
    return track[l]

COMPTEUR = 0
print(decoupe_BU(longueur, prix))
print(COMPTEUR)