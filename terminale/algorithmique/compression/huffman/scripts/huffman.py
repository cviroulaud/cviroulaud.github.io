#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 29 Septembre 2021 10:32
"""

import doctest


class Noeud:
    def __init__(self, f: int, l: str, g=None, d=None):
        # lettre ne prend une valeur que si on est sur une feuille
        self.lettre = l
        self.f = f
        # valeur du codage
        self.val = 0
        self.gauche = g
        self.droite = d


def calculer_frequence(mot: str) -> list:
    """
    renvoie la liste triée de la fréquence de chaque lettre

    Args:
        mot (str): mot à compresser

    Returns:
        list: tuple(lettre, fréquence)

    >>> calcul_frequence("aabacc")
    [('a', 3), ('c', 2), ('b', 1)]
    """
    res = {}
    for l in mot:
        if l in res:
            res[l] += 1
        else:
            res[l] = 1
    t = []
    for l, f in res.items():
        t.append((l, f))
    t.sort(key=lambda e: e[1], reverse=True)
    return t


def creer_arbre(mot: str) -> Noeud:
    f = calculer_frequence(mot)
    # forêt de noeuds triée
    foret = [Noeud(e[1], e[0]) for e in f]
    while len(foret) > 1:
        n1 = foret.pop()
        n2 = foret.pop()
        # n1 est forcément <= n2
        n1.val = 0
        n2.val = 1
        n = Noeud(n1.f+n2.f, "", n1, n2)
        # ajoute en fin
        foret.append(n)
        # remonte pour garder foret triée
        i = len(foret)-1
        while i > 0 and foret[i].f < foret[i-1].f:
            foret[i], foret[i-1] = foret[i-1], foret[i]
            i -= 1
    return foret[0]


def creer_codage(arbre: Noeud, code: str, acc: dict) -> None:
    if arbre.gauche is None:  # droite aussi = feuille
        acc[arbre.lettre] = code
    else:
        creer_codage(arbre.gauche, code+"0", acc)
        creer_codage(arbre.droite, code+"1", acc)


def codage_huffman(arbre: Noeud, mot: str) -> str:
    codage = {}
    creer_codage(arbre, "", codage)
    code = ""
    for l in mot:
        code += codage[l]
    return code


def decodage_huffman(arbre: Noeud, code: str) -> str:
    mot = ""
    while len(code) > 0:
        enc = arbre
        while enc.gauche is not None:
            val, code = int(code[:1]), code[1:]
            if val == 0:
                enc = enc.gauche
            else:
                enc = enc.droite
        mot += enc.lettre
    return mot


doctest.testmod(verbose=True)
mot = "anticonstitutionnellement"
arbre = creer_arbre(mot)
c = codage_huffman(arbre, mot)
print(c)
print(decodage_huffman(arbre, c))
