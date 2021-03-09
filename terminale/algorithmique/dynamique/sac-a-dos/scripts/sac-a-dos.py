#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/09 12:04:13
"""


def sac_naif(masses: list, valeurs: list, limite: int)->int:
    """
    sac à dos avec remise
    """
    if limite == 0:
        return 0
    val_max = 0
    for i in range(len(masses)):
        if masses[i] <= limite:
            val = valeurs[i] + sac_naif(masses, valeurs, limite-masses[i])
            if val > val_max:
                val_max = val
    return val_max
    
limite = 7
masses = [5, 3, 1, 4]
valeurs = [100, 55, 18, 70]
print(sac_naif(masses, valeurs, limite))