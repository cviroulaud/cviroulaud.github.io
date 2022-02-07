#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 28 Janvier 2022 23:43
"""
import json


def profondeur(graphe: dict, noeud: str, visites: list) -> None:
    if noeud not in visites:
        print(noeud, end=" ")
        visites.append(noeud)
        for voisin in graphe[noeud]:
            profondeur(graphe, voisin, visites)


def est_connexe(graphe: dict, depart: int) -> bool:
    visites = []
    profondeur(graphe, depart, visites)
    return len(graphe) == len(visites)


f = open("parcours_noir.json")
donnees = json.load(f)  # tableau de dictionnaires
graphe = {}
for info in donnees:
    sommet = info["sommet"]
    adjacents = info["adjacents"]
    graphe[sommet] = adjacents
f.close()
print(est_connexe(graphe, 70))
