#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 16 14:10:12 2020

@auteur: Christophe Viroulaud
"""


from mod_pile import Pile

def bien_parenthesee(code: str)->bool:
    parentheses = Pile()
    taille = len(code)
    i = 0
    correct = True
    while i < taille and correct:
        if code[i] == "(":
            parentheses.empiler("(")
        elif code[i] == ")":
            if parentheses.depiler() is None:
                correct = False
        i += 1

    return correct

chaine_correcte = "((e)ee(e))"
chaine_incorrecte = "(e))"

print(bien_parenthesee(chaine_correcte))
print(bien_parenthesee(chaine_incorrecte))