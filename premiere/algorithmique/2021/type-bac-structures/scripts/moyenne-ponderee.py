#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/12 13:33:14
"""


def moyenne(notes: list) -> int:
    """
    calcule la moyenne pondérée des notes

    Args:
        notes (list): liste de tuples (note, coef)

    Returns:
        int: moyenne
    """
    assert len(notes) > 0, "Il faut au moins une note."
    somme = 0
    coefficients = 0
    for couple in notes:
        somme += couple[0]*couple[1]
        coefficients += couple[1]
    print(somme, coefficients)
    return somme/coefficients


notes = [(15, 2), (9, 1), (12, 3)]
print(moyenne(notes))
