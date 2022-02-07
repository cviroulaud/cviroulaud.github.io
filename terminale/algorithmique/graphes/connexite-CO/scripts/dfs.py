#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 05 Février 2022 21:54
"""


def profondeur(graphe: dict, noeud: str, visites: list) -> None:
    if noeud not in visites:
        print(noeud, end=" ")
        visites.append(noeud)
        for voisin in graphe[noeud]:
            profondeur(graphe, voisin, visites)


graphe = {"A": ["C", "H", "J"],
          "B": ["E"],
          "C": ["A", "D", "E"],
          "D": ["C", "F", "J"],
          "E": ["B", "C"],
          "F": ["D"],
          "G": ["H"],
          "H": ["A", "G", "I"],
          "I": ["H"],
          "J": ["A", "D"]}
profondeur(graphe, "I", [])
