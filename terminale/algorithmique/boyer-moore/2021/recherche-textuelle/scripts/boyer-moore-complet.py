#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 27 Septembre 2021 23:07
"""
import doctest
from collections import defaultdict


def bad_char(motif: str) -> dict:
    """
    position du "mauvais caractère"
    nb sur wikipedia on calcule la distance / fin motif --> Horspool
    """
    # pour avoir -1 pour tous les caractères non présents dans motif    
    bad = defaultdict(lambda: -1)
    for i in range(len(motif)-1):
        bad[motif[i]] = i
    return bad


def set_suffixe(motif: str) -> list:
    """
    position du début du plus long suffixe = au suffixe 
    avec lettre précédente différente

    >>> set_suffixe("abaaaa")
    [-1, -1, -1, 2, 2, 2, 5]
    """
    s = [-1 for _ in range(len(motif)+1)]
    for j in range(1, len(motif)):
        suffixe = motif[j:]
        k = j-1
        while k >= 0:
            if suffixe == motif[k:k+len(suffixe)]:
                if k == 0 or motif[j-1] != motif[k-1]:
                    """
                    on est au début de motif: la 'lettre précédente' est différente (convention)
                    OU la lettre précédente est différente
                    rq: évaluation paresseuse: on vérifie d'abord k==0
                    """
                    s[j] = k
                    k = -1  # pour sortir de la boucle
                else:
                    # même lettre avant le suffixe (pas bon)
                    k -= 1
            else:
                k -= 1
    s[len(motif)] = len(motif)-1
    return s


def set_prefixe(motif: str) -> list:
    """
    longueur du plus long préfixe qui soit aussi
    suffixe de suffixe

    >>> set_prefixe("abaaaa")
    [1, 1, 1, 1, 1, 1]
    """
    p = [0 for _ in range(len(motif))]
    # pour chaque suffixe
    for j in range(1, len(motif)):
        k = j
        suffixe = motif[k:]
        # regarde tous les sous-suffixes
        while len(suffixe) > 0 and suffixe != motif[:len(suffixe)]:
            k += 1
            suffixe = motif[k:]
        p[j] = len(suffixe)
    p[0] = p[1]
    return p


def boyer_moore(chaine: str, motif: str) -> int:
    """
    renvoie l'indice de la 1ere position de motif
    -1 sinon

    >>> boyer_moore("anpanman","an")
    [0, 3, 6]

    >>> boyer_moore("abbcaacaaaabaaaa","dd")
    []

    >>> boyer_moore("abbcaacaaaabaaaa","abaaaa")
    [10]
    """
    d = bad_char(motif)
    s = set_suffixe(motif)
    p = set_prefixe(motif)
    positions = []
    i = 0
    # tant qu'on n'a pas parcouru toute la chaine
    while i <= len(chaine)-len(motif):
        j = len(motif)-1
        # comparaison à reculons
        while j >= 0 and chaine[i+j] == motif[j]:
            j -= 1
        if j == -1:  # on a trouvé
            positions.append(i)
            i = i+len(motif)-p[1]
        else:  # fait le (meilleur) saut
            if s[j+1] >= 0:
                # ya un suffixe
                i = i+max(j+1-s[j+1], j-d[chaine[i+j]])
            else:
                # prend préfixe
                i = i+max(len(motif)-p[j], j-d[[chaine[i+j]]])
    return positions


doctest.testmod(verbose=True)
