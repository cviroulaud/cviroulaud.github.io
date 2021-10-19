#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 19 Octobre 2021 13:06
"""

from pile import Pile


def bien_parenthesee(code: str) -> bool:
    parentheses = Pile()
    i = 0
    correct = True
    while i < len(code) and correct:
        # empile une ouvrante
        if code[i] == "(":
            parentheses.empiler("(")
        # dépile une ouvrante quand on trouve une fermante
        elif code[i] == ")":
            # si rien à dépiler -> mauvais parenthésage
            if parentheses.depiler() is None:
                correct = False
        i += 1

    return correct


def bien_parenthesee_rec(code: str, i: int, p: Pile) -> bool:
    if i == len(code):
        return True
    else:
        if code[i] == "(":
            p.empiler("(")
        elif code[i] == ")":
            if p.depiler() is None:
                return False
        return bien_parenthesee_rec(code, i+1, p)


chaine_correcte = "((e)ee(e))"
chaine_incorrecte = "(e))"

print(bien_parenthesee(chaine_correcte))
print(bien_parenthesee(chaine_incorrecte))

print(bien_parenthesee_rec(chaine_correcte, 0, Pile()))
print(bien_parenthesee_rec(chaine_incorrecte, 0, Pile()))
