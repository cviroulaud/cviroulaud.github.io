#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 15:36:07 2021

@auteur: Christophe Viroulaud
"""


def est_majeur2(age: int) -> bool:
    """
    vérifie si la personne est majeur

    Parameters
    ----------
    age : int
        âge de la personne.
    Returns
    -------
    boolean

    """
    return age >= 18


def est_majeur(age: int) -> bool:
    """
    vérifie si la personne est majeur

    Args:
        age (int): âge de la personne

    Returns:
        bool: True si majeur
    """
    if age >= 18:
        return True
    else:
        return False
