#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 16:31:49 2020

@auteur: Christophe Viroulaud
"""


epaisseur = 0.1
pli = 0
while epaisseur < 324:
    epaisseur *= 2
    # ou bien
    # epaisseur = epaisseur * 2
    pli += 1

print(pli)
