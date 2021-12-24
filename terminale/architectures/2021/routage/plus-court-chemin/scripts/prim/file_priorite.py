#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/06 12:57:46
"""


class Noeud:
    def __init__(self, nom: str):
        self.nom = nom
        self.cout = float("inf")
        self.pred = None

    def __str__(self):
        return self.nom + " "+str(self.cout)+" "+self.pred


def enfiler(l: list, s: dict, nom: str) -> None:
    """
    la file contient les noms des sommets
    à rapprocher du dict 's' contenant les coûts
    """
    # ajoute à la fin
    l.append(nom)
    # remonte
    i_fils = len(l)-1
    i_pere = (i_fils-1)//2
    #i_fils=0 --> on est remonté à la racine
    while i_fils > 0 and s[l[i_fils]].cout < s[l[i_pere]].cout:
        l[i_pere], l[i_fils] = l[i_fils], l[i_pere]
        i_fils = i_pere
        i_pere = (i_fils-1)//2


def get_fils_mini(l: list, s: dict, i: int) -> int:
    i_fils = 2*i+1
    if i_fils >= len(l):
        return -1
    if i_fils == len(l)-1:
        return i_fils
    if s[l[i_fils]].cout > s[l[i_fils+1]].cout:
        i_fils += 1
    return i_fils


def defiler(l: list, s: dict) -> str:
    # à renvoyer
    res = l[0]
    # remonte dernier à la racine
    l[0] = l[len(l)-1]
    l.pop()
    # redescend
    i_pere = 0
    i_fils = get_fils_mini(l, s, i_pere)
    #i_fils > 0 car get_fils_mini renvoie -1 si on sort de la list
    while i_fils > 0 and s[l[i_fils]].cout < s[l[i_pere]].cout:
        l[i_pere], l[i_fils] = l[i_fils], l[i_pere]
        i_pere = i_fils
        i_fils = get_fils_mini(l, s, i_pere)
    return res


def maj_file(l: list, s: dict, n: str) -> None:
    # trouve la position de n
    i_fils = 0
    while l[i_fils] != n:
        i_fils += 1

    # maj la liste
    # remonte
    i_pere = (i_fils-1)//2
    while i_fils == 0 or s[l[i_fils]].cout < s[l[i_pere]].cout:
        l[i_pere], l[i_fils] = l[i_fils], l[i_pere]
        i_fils = i_pere
        i_pere = (i_fils-1)//2
