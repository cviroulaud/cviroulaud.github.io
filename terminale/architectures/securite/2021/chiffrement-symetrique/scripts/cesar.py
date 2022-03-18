#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/20 16:08:18
"""


def chiffrement(message: str, cle: int) -> str:
    sortie = ""
    for lettre in message:
        sortie += chr(ord(lettre)+cle)
    return sortie


def dechiffrement(message: str, cle: int) -> str:
    sortie = ""
    for lettre in message:
        sortie += chr(ord(lettre)-cle)
    return sortie


k = 3
entree = "LANSIESTFANTASTIQUE"
m_chiffre = chiffrement(entree, k)
print(m_chiffre)
print(dechiffrement(m_chiffre, k))
