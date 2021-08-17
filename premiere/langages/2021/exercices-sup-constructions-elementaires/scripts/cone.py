#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 15:55:19 2020

@auteur: Christophe Viroulaud
"""


from math import pi

rayon = int(input("rayon: "))
hauteur = int(input("hauteur: "))
volume = pi * rayon**2 * hauteur/3
print(volume)