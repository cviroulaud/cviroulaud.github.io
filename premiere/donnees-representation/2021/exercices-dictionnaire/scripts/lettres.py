#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/24 22:26:44
"""

def lettres(mot: str)->dict:
    """
    compte le nombre d'occurrences
    de chaque lettre du mot
    """
    occurrences = {}
    for l in mot:
        # si la lettre est déjà référencée
        if l in occurrences:
            occurrences[l] += 1
        else:
            occurrences[l] = 1
    return occurrences

print(lettres("bonjour"))