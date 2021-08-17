#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Feb  4 15:01:47 2021

@auteur: Christophe Viroulaud
"""


def calcul_remise(prix, remise):
    """
    calcule la valeur de la remise en euro

    Parameters
    ----------
    prix : int
        prix non soldé.
    remise : str
        nom de l'étiquette.

    Returns
    -------
    valeur de la remise.

    """
    if remise == "rouge":
        return prix*0.30
    elif remise == "verte":
        return prix*0.40
    elif remise == "bleue":
        return prix*0.50
    else: # pas de remise
        return 0