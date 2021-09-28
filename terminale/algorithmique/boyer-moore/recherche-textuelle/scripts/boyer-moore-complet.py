#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 27 Septembre 2021 23:07
"""


def bad_char(motif: str) -> dict:
    """
    crée la table "mauvais caractère"
    """
    bad = {}
    for i in range(len(motif)-1):
        bad[motif[i]] = len(motif)-1-i
    return bad


def good_suffix(motif: str) -> dict:
    """
    crée la table "bon suffixe"
    """
    good = {}
    for i in range(len(motif)):
        suffixe = motif[i:]
        # on essaie de trouver une répétition du suffixe 'avant"
        j = i-len(suffixe)
        while j >= 0 and suffixe != motif[j:j+len(suffixe)] and motif[i-1] != motif[j-1]:
            j -= 1
        if j < 0:  # on n'a pas trouvé
            # on cherche le plus grand préfixe
            prefixe = motif[:len(suffixe)]
            while len(suffixe) > 0 and prefixe != suffixe:
                suffixe = suffixe[1:]
                prefixe = motif[:len(suffixe)]
            good[suffixe] = len(motif)-len(suffixe)
        else:  # on a trouvé
            good[suffixe] = len(motif)-(j+len(suffixe))
    return good


def boyer_moore(chaine: str, motif: str) -> int:
    """
    renvoie l'indice de la 1ere position de motif
    -1 sinon
    """
    bad = bad_char(motif)
    good = good_suffix(motif)
    positions=[]
    i = 0
    # tant qu'on n'a pas parcouru toute la chaine
    while i < len(chaine)-len(motif):
        j = len(motif)-1
        # comparaison à reculons
        while j>=0 and chaine[i+j] == motif[j]:
            j -= 1
        if j=-1:  # on a trouvé
            positions.append(i)
        else:  # fait le (meilleur) saut
            deb += max(bad[chaine[fin]], good[chaine[fin:fin+taille]])
    return -1


c = "anpanman"
m = "an"
print(boyer_moore(c,m))