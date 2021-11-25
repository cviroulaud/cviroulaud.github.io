#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 24 Septembre 2021 09:07
"""


def bf(mat: list, depart: int, arrivee: int) -> list:
    distances = [{"dist": float("inf"), "pred": None} for _ in range(len(mat))]
    distances[0]["dist"] = 0
    modif = True
    while modif: #ERREUR devrait être la 1° boucle for
        modif = False
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] != 0:  # il y a un arc
                    dist_calc = distances[i]["dist"]+mat[i][j]
                    if dist_calc < distances[j]["dist"]:
                        distances[j]["dist"] = dist_calc
                        distances[j]["pred"] = i
                        modif = True
    
    # reconstruction chemin
    return reconstruction(distances, depart, arrivee)
    """
    chemin = []
    while arrivee != depart:
        chemin.append((arrivee, distances[arrivee]["dist"]))
        arrivee = distances[arrivee]["pred"]
    chemin.append((depart, 0))
    chemin.reverse()
    return chemin
    """


def reconstruction(distances: list, d: int, a: int) -> str:
    if a == d:
        return str(d)
    else:
        return reconstruction(distances, d, distances[a]["pred"])+f" - {a}"


mat = [[0, 10, 0, 0, 0, 8],
       [0, 0, 0, 2, 0, 0],
       [0, 2, 0, 0, 0, 0],
       [0, 0, -2, 0, 0, 0],
       [0, -4, 0, -1, 0, 0],
       [0, 0, 0, 0, 1, 0]]

print(bf(mat, 0, 3))
