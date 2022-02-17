#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Monday 14 February 2022 11:04
"""
BLANC, GRIS, NOIR = 0, 1, 2


def dfs(graphe: list, sommet: int, visites: list) -> None:
    # en cours de parcours
    visites[sommet]["coul"] = GRIS
    for voisin in graphe[sommet]:
        # pour chaque voisin non encore atteint
        if visites[voisin]["coul"] == BLANC:
            visites[voisin]["pred"] = sommet
            dfs(graphe, voisin, visites)
    # parcours terminé pour ce sommet
    visites[sommet]["coul"] = NOIR


def parcours(graphe: list) -> list:
    visites = [{"coul": BLANC, "pred": None} for i in range(len(graphe))]
    for i in range(len(graphe)):
        if visites[i]["coul"] == BLANC:
            dfs(graphe, i, visites)
    return visites


graphe = [[1, 2],
          [3],
          [5],
          [0, 2, 6],
          [1],
          [4],
          [],
          [2]]
print(parcours(graphe))
