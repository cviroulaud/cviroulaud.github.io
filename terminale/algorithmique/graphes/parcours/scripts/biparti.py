#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 22 Septembre 2021 13:19
"""

from collections import deque

NOIR, GRIS, BLANC = 2, 1, 0
INCOLORE, ROUGE, BLEU = 0, 1, 2


def bfs(l: dict, dep: int) -> list:
    visites = []
    f = deque()
    f.appendleft(dep)
    visites.append(dep)

    while f:
        enc = f.pop()
        for v in l[enc]:
            if v not in visites:
                visites.append(v)
                f.appendleft(v)
    return visites


def bfs2(l: dict, dep: int) -> list:
    noeuds = {i: {"dist": 0, "couleur": BLANC, "pred": None} for i in l.keys()}
    f = deque()
    f.appendleft(dep)
    noeuds[dep]["couleur"] = GRIS

    while f:
        enc = f.pop()
        for v in l[enc]:
            if noeuds[v]["couleur"] == BLANC:
                noeuds[v]["couleur"] = GRIS
                noeuds[v]["dist"] = noeuds[enc]["dist"]+1
                noeuds[v]["pred"] = enc
                f.appendleft(v)
        noeuds[enc]["couleur"] = NOIR
    return noeuds


def has_cycle(l: dict, dep: int) -> bool:
    noeuds = {i: {"dist": 0, "couleur": BLANC, "pred": None} for i in l.keys()}
    f = deque()
    f.appendleft(dep)
    noeuds[dep]["couleur"] = GRIS

    while f:
        enc = f.pop()
        for v in l[enc]:
            if noeuds[v]["couleur"] == GRIS:
                return True
            if noeuds[v]["couleur"] == BLANC:
                noeuds[v]["couleur"] = GRIS
                noeuds[v]["dist"] = noeuds[enc]["dist"]+1
                noeuds[v]["pred"] = enc
                f.appendleft(v)
        noeuds[enc]["couleur"] = NOIR
    return False


def biparti(l: dict, dep: int) -> dict:
    noeuds = {i: {"dist": 0, "couleur": BLANC, "pred": None, "bicol": 0}
              for i in l.keys()}

    # parcours en largeur
    f = deque()
    f.appendleft(dep)
    noeuds[dep]["couleur"] = GRIS
    noeuds[dep]["bicol"] = ROUGE

    while f:
        enc = f.pop()
        for v in l[enc]:
            if noeuds[v]["couleur"] == BLANC:
                noeuds[v]["couleur"] = GRIS
                noeuds[v]["dist"] = noeuds[enc]["dist"]+1
                noeuds[v]["pred"] = enc
                if noeuds[enc]["bicol"] == ROUGE:
                    noeuds[v]["bicol"] = BLEU
                else:
                    noeuds[v]["bicol"] = ROUGE
                f.appendleft(v)
        noeuds[enc]["couleur"] = NOIR

    # détecte biparti: pas d'arête entre sommets de couleurs identiques
    # = couleurs différentes entre voisins
    for n in noeuds.keys():
        couleur = noeuds[n]["bicol"]
        for v in l[n]:
            if noeuds[v]["bicol"] == couleur:
                return False
    return True


def biparti2(l: dict, dep: int) -> dict:
    """
    avec un seul parcours
    """
    noeuds = {i: {"dist": 0, "couleur": BLANC, "pred": None, "bicol": 0}
              for i in l.keys()}

    # parcours en largeur
    f = deque()
    f.appendleft(dep)
    noeuds[dep]["couleur"] = GRIS
    noeuds[dep]["bicol"] = ROUGE

    while f:
        enc = f.pop()
        couleur_suiv = noeuds[enc]["bicol"] % 2 + 1
        for v in l[enc]:
            if noeuds[v]["couleur"] == GRIS:
                if noeuds[v]["bicol"] != couleur_suiv:
                    return False
            if noeuds[v]["couleur"] == BLANC:
                noeuds[v]["couleur"] = GRIS
                noeuds[v]["dist"] = noeuds[enc]["dist"]+1
                noeuds[v]["pred"] = enc
                # 1ere visite on le colore
                noeuds[v]["bicol"] = couleur_suiv
                f.appendleft(v)
        noeuds[enc]["couleur"] = NOIR
    return True


l = {
    1: {2, 3},
    2: {1, 4, 5,3},
    3: {1, 5, 10,2},
    4: {2, 6},
    5: {2, 3, 6},
    6: {4, 5, 7},
    7: {6, 8},
    8: {7, 9, 10},
    9: set(),
    10: {3, 8}
}

print("bfs", bfs(l, 1))
#print(bfs2(l, 1))
print("has_cycle", has_cycle(l, 1))
print("biparti", biparti(l, 1))
print("biparti2", biparti2(l, 1))
