#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Monday 14 February 2022 16:06
"""

"""
cas particulier du sac à dos où:
    poids = somme
    valeur = 1 pour toutes les pièces
    cherche à minimiser valeur (nb pièces)
"""
def nb_pieces(somme: int, systeme: list) -> int:
    track = [somme+1 for _ in range(somme+1)]
    track[0] = 0
    for x in range(1, somme+1):
        for piece in systeme:
            if piece <= x:
                track[x] = min(track[x], 1+track[x-piece])

    return track


systeme = [10, 5, 2, 1]
somme = 8
print(nb_pieces(somme, systeme))
