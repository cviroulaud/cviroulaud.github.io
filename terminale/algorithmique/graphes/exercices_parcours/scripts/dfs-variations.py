#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Monday 14 February 2022 10:21
"""


def profondeur_dict(graphe: dict, noeud: str, visites: dict) -> None:
    if not visites[noeud]:
        print(noeud, end=" ")
        visites[noeud] = True
        for voisin in graphe[noeud]:
            profondeur_dict(graphe, voisin, visites)


def get_indice(sommet: str) -> int:
    return ord(sommet)-65


def profondeur_tab(graphe: dict, noeud: str, visites: dict) -> None:
    ind = get_indice(noeud)
    if not visites[ind]:
        print(noeud, end=" ")
        visites[ind] = True
        for voisin in graphe[noeud]:
            profondeur_tab(graphe, voisin, visites)


graphe = {"A": ["B", "C", "D"],
          "B": ["A", "D", "E"],
          "C": ["A", "D", "F", "H"],
          "D": ["A", "B", "C", "G"],
          "E": ["B", "F"],
          "F": ["C", "E"],
          "G": ["D"],
          "H": ["C"]}

visites_dico = {chr(65+i): False for i in range(8)}
profondeur_dict(graphe, "A", visites_dico)

visites_tab = [False for i in range(8)]
profondeur_tab(graphe, "A", visites_tab)
