#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Oct 17 12:00:04 2020

@auteur: Christophe Viroulaud
"""

mini = 1
maxi = 100
trouve = False
coups = 0

print("Pensez à un nombre entre 1 et 100.")
while not trouve:
    coups += 1
    proposition = (mini + maxi)//2
    print("Le nombre est-il {}?".format(proposition))
    reponse = input("Merci de répondre = + ou -: ")
    if reponse == "=":
        print("J'ai trouvé en {} coups!".format(coups))
        trouve = True
    elif reponse == "+":
        mini = proposition
    else:
        maxi = proposition
