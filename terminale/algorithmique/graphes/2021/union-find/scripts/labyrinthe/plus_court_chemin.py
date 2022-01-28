#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/05 00:20:37
"""

from collections import deque


def set_dico(laby: set) -> dict:
    """
    laby est un ensemble de tuples
    (coord_n1, coord_n2)
    """
    dico = {}
    for a in laby:
        if a[0] not in dico:  # noeud n'est pas encore dans dico
            dico[a[0]] = set()
        # ne rajoute pas de doublon (car set)
        dico[a[0]].add(a[1])
        if a[1] not in dico:  # symétrie
            dico[a[1]] = set()
        dico[a[1]].add(a[0])
    return dico


def bfs(laby: set):
    # transforme l'ensemble des arêtes en 1 dico d'adjacence des sommets
    dico_voisins = set_dico(laby)

    visites = set()
    predecesseurs = {(0, 0): None}
    f = deque()
    f.appendleft((0, 0))

    # tant que la liste n'est pas vide
    while f:
        n = f.pop()        
        visites.add(n)
        for voisin in dico_voisins[n]:
            if voisin not in visites:
                """
                dijkstra (différence):
                    on utilise une file de priorité
                    (pour toujours prendre le noeud avec
                    la + petite distance)
                    on calcule et met à jour la distance
                    dans 'predecesseurs'
                """
                f.appendleft(voisin)
                predecesseurs[voisin] = n
    return predecesseurs
