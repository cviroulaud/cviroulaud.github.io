#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Oct 17 15:13:49 2020

@auteur: Christophe Viroulaud
"""


nb = int(input("Quelle table voulez-vous afficher? "))
for i in range(11): # 11 signifie qu'il il y aura 11 tours
    """
    Noter ici le f en début de ligne qui est une autre manière de
    formater le texte. Ceci ne fonctionne que pour des versions
    récentes de Python (>=3.6). Il est possible d'écrire:
        print("{}×{} = {}".format(i,nb,i*nb))
    """
    print(f"{i}×{nb} = {i*nb}")