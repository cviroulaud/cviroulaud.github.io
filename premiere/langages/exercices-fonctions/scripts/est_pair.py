#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 15:10:20 2021

@auteur: Christophe Viroulaud
"""


def est_pair(x):
    """
    vérifie la parité

    Parameters
    ----------
    x : int

    Returns
    -------
    boolean
    """
    return x%2 == 0

print(est_pair(11))