#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 24 Octobre 2021 15:47
"""


def meilleure_perf(tab: list) -> float:
    """
    renvoie la plus grande valeur du tableau
    """
    meilleure = 0
    for perf in tab:
        if perf > meilleure:
            meilleure = perf

    return meilleure


def moyenne(tab: list) -> float:
    """
    calcule la moyenne des valeurs
    du tableau.
    Les 0 ne sont pas pris en compte.
    """
    somme = 0
    nb_sauts = 0
    for perf in tab:
        if perf > 0:
            somme += perf
            nb_sauts += 1

    # si tous les sauts sont ratés
    if nb_sauts == 0:
        return 0
    else:
        return somme/nb_sauts


lewis = [0., 0., 0., 0., 0., 0.]
powell = [0., 0., 0., 0., 0., 0.]
print("Carl Lewis", lewis)
print("Mike Powell", powell)

# 1er saut
lewis[0] = 8.68
powell[0] = 7.85
print("Carl Lewis", lewis)
print("Mike Powell", powell)

# 2eme saut
lewis[1] = 0.
powell[1] = 8.54
print("Carl Lewis", lewis)
print("Mike Powell", powell)

# 3eme saut
lewis[2] = 8.83
powell[2] = 8.29
print("Carl Lewis", lewis)
print("Mike Powell", powell)

# 4eme saut
lewis[3] = 8.91
powell[3] = 0.
print("Carl Lewis", lewis)
print("Mike Powell", powell)

# 5eme saut
lewis[4] = 8.87
powell[4] = 8.95
print("Carl Lewis", lewis)
print("Mike Powell", powell)

# 6eme saut
lewis[5] = 8.84
powell[5] = 0.
print("Carl Lewis", lewis)
print("Mike Powell", powell)

print(meilleure_perf(powell))
print(moyenne(powell))
print(meilleure_perf(lewis))
print(moyenne(lewis))
