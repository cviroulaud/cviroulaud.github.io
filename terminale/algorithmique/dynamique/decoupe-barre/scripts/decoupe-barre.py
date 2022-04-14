#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/11 09:14:48
"""


def decoupe_naif(l: int, prix: dict) -> int:
    """
    renvoie le prix maximum pour une barre de taille l
    """
    if l == 0:
        return 0
    val_max = 0
    for taille, valeur in prix.items():
        if l >= taille:
            val_calc = decoupe_naif(l-taille, prix) + valeur
            if val_calc > val_max:
                val_max = val_calc
    return val_max


longueur = 10
# prix correspondant à chaque taille de découpe
prix = {1: 2, 2: 5, 3: 8, 4: 10, 5: 11, 6: 14, 8: 17, 10: 20}
print(decoupe_naif(longueur, prix))


def decoupe_TD(l: int, prix: dict, track: list) -> int:
    """
    renvoie le prix maximum pour une barre de taille l
    """
    if track[l] > 0:
        return track[l]
    if l == 0:  
        return track[0]
    val_max = 0
    for taille, valeur in prix.items():
        if l >= taille:
            val_calc = decoupe_TD(l-taille, prix, track) + valeur
            if val_calc > val_max:
                val_max = val_calc
    track[l] = val_max
    return track[l]


track = [0 for _ in range(longueur+1)]
print(decoupe_TD(longueur, prix, track))


def decoupe_BU(l: int, prix: dict) -> int:
    track = [0 for _ in range(l+1)]
    # calcule le prix pour chaque longueur en partant des petites valeurs
    for i in range(1, l+1):
        val_max = 0
        for taille, valeur in prix.items():
            if i >= taille:
                val_calc = track[i-taille] + valeur
                if val_calc > val_max:
                    val_max = val_calc
        track[i] = val_max
    return track[l]


print(decoupe_BU(longueur, prix))
