#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/05/10 16:36:16
"""


def pretraitement_decalages(motif: str) -> dict:
    """
    renvoie le dictionnaire des décalages à appliquer
    pour chaque lettre du motif (sauf dernière)
    """
    decalages = dict()
    # on s'arrête à l'avant dernière lettre du motif
    for i in range(len(motif)-1):
        # len(motif)-1 est la position de la dernière lettre
        decalages[motif[i]] = len(motif)-1-i
    return decalages


def decalage_fenetre(decalages: dict, taille: int, lettre: str) -> int:
    """
    renvoie la valeur du décalage à appliquer.
    si la lettre n'est pas dans le tableau
    c'est la taille du motif qui est appliqué

    Args:
        decalages (dict): dico des décalages
        taille (int): taille du motif (= décalage max)
        lettre (str): dernière lettre de la fenêtre

    Returns:
        int: décalage à appliquer
    """
    for cle, val in decalages.items():
        if cle == lettre:
            return val
    # si la lettre n'est pas dans le dico (= le motif)
    return taille


def decalage_fenetre2(decalages: dict, taille: int, lettre: str) -> int:
    # la méthode get renvoie une valeur par défaut si elle ne trouve pas la clé
    return decalages.get(lettre, taille)


def decalage_fenetre3(decalages: dict, taille: int, lettre: str) -> int:
    try:
        res = decalages[lettre]
    except KeyError:
        res = taille
    return res


def compare(texte: str, position: int, motif: str) -> bool:
    """
    compare le morceau du texte 
    (en partant de position + taille(motif)) 
    avec le motif

    Returns:
        bool: True si on a trouvé le motif
    """
    # position de la dernière lettre de la fenêtre
    en_cours = position+len(motif)-1
    # parcours de la fenêtre à l'envers
    for i in range(len(motif)-1, -1, -1):
        if not(texte[en_cours] == motif[i]):
            return False
        else:
            en_cours -= 1
    return True


def boyer_moore(texte: str, motif: str) -> int:
    """
    Returns:
        int: la position du motif dans le texte, -1 sinon.
    """
    decalages = pretraitement_decalages(motif)
    i = 0
    while i <= len(texte)-len(motif):
        # si on trouve le motif
        if compare(texte, i, motif):
            return i
        else:
            # sinon on décale (en fonction de la dernière lettre de la fenêtre)
            decale = decalage_fenetre(decalages, 
                                       len(motif), 
                                       texte[i+len(motif)-1])
            i += decale
    # si on sort de la boucle, on n'a rien trouvé
    return -1


t = "atgatccatga"
m = "cat"
print(boyer_moore(t, m))
t="stupid_spring_ring"
m="ring_ring"
print(boyer_moore(t, m))
