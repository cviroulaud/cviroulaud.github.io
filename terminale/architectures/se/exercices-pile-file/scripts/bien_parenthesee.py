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

    while i < len(code):
        # empile une ouvrante
        if code[i] == "(":
            parentheses.empiler("(")
        # dépile une ouvrante quand on trouve une fermante
        elif code[i] == ")":
            # si rien à dépiler -> mauvais parenthésage
            if parentheses.depiler() is None:
                return False
        i += 1

    # si la pile n'est pas vide: il reste des (
    return parentheses.est_vide()


def bien_parenthesee_rec(code: str, i: int, p: Pile) -> bool:
    if i == len(code):
        # si la pile n'est pas vide: il reste des (
        return p.est_vide()
    else:
        if code[i] == "(":
            p.empiler("(")
        elif code[i] == ")":
            if p.depiler() is None:
                return False
        return bien_parenthesee_rec(code, i+1, p)


chaine_correcte = "((e)ee(e))"
chaine_incorrecte = "(((e))"
chaine_incorrecte2 = "((e)))"


print(bien_parenthesee(chaine_correcte))
print(bien_parenthesee(chaine_incorrecte))
print(bien_parenthesee(chaine_incorrecte2))

print(bien_parenthesee_rec(chaine_correcte, 0, Pile()))
print(bien_parenthesee_rec(chaine_incorrecte, 0, Pile()))
print(bien_parenthesee_rec(chaine_incorrecte2, 0, Pile()))
