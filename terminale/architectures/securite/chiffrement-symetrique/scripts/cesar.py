#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 18 Mars 2022 15:33
"""


def chiffrement(message: str, cle: int) -> str:
    sortie = ""
    for lettre in message:
        # code ASCII de la lettre chiffrée
        code = ord(lettre) + cle
        # ajout
        sortie = sortie+chr(code)
    return sortie


def chiffrement2(message: str, cle: int) -> str:
    sortie = ""
    for lettre in message:
        # code ASCII de la lettre chiffrée
        code = (ord(lettre) + cle)
        # ajustement du code ASCII
        if code > ord("Z"):
            code = code-26
        # ajout
        sortie = sortie+chr(code)
    return sortie


def dechiffrement(secret: str, cle: int) -> str:
    sortie = ""
    for lettre in secret:
        # code ASCII de la lettre chiffrée
        code = ord(lettre) - cle
        # ajustement du code ASCII
        if code < ord("A"):
            code = code+26
        # ajout
        sortie = sortie+chr(code)
    return sortie


print(chiffrement2("NSI", 13))
print(chiffrement2("AFV", 13))
