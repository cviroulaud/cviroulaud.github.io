#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 12 Décembre 2021 12:19
"""
from random import randint


def est_present(tab: list, e: int) -> bool:
    """
    vérifie si e est dans le tableau
    """
    for val in tab:
        if val == e:
            return True
    # On est sorti de la boucle sans avoir trouvé
    return False


tab = [randint(1, 100) for _ in range(10)]
print(tab)
print(maximum(tab))
print(maximum2(tab))
