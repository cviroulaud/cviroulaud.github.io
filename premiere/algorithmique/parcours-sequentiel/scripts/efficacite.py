#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/14 13:26:46
"""


def est_present(tab: list, note: int)->bool:
    """
    vérifie si note est dans le tableau
    """
    for n in tab:
        if n == note:
            return True
    # On est sorti de la boucle sans avoir trouvé note
    return False

def moyenne(tab: list)->float:
    somme = 0
    for n in tab:
        somme += n
    return somme/len(tab)

from random import randint

les_notes = [randint(0, 20) for _ in range(30)]
print(les_notes)
print(est_present(les_notes, 15))
print(moyenne(les_notes))