#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/05/20 16:56:52
"""

from random import randint


def recherche_classique(tab: list, cherche: int) -> bool:
    """
    Renvoie True si 'cherche' est dans 'tab'
    """
    for element in tab:
        if element == cherche:
            return True
    # à la fin de la boucle on n'a pas trouvé 'cherche'
    return False


def recherche_dicho(tab: list, cherche: int) -> bool:
    i_debut = 0
    i_fin = len(tab)-1
    while i_fin >= i_debut:
        i_milieu = (i_debut+i_fin) // 2
        if cherche == tab[i_milieu]:
            return True
        elif cherche < tab[i_milieu]:
            i_fin = i_milieu-1
        else:  # cherche > tab[i_milieu]
            i_debut = i_milieu+1
    # à la fin de la boucle on n'a pas trouvé 'cherche'
    return False


entiers = [randint(0, 1000000) for _ in range(100000)]


print(recherche_classique(entiers, 575000))

entiers.sort()
print(recherche_dicho(entiers, 575000))
