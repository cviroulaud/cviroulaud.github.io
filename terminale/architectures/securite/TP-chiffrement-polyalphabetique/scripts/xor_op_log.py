#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 20 Mars 2022 17:09
"""


def str_en_int(texte: str, taille: int) -> list:
    """
    renvoie le tableau des valeurs ASCII d'un texte
    """
    texte_ascii = [0 for _ in range(taille)]
    for i in range(taille):
        texte_ascii[i] = ord(texte[i % len(texte)])
    return texte_ascii


def chiffrement(message: str, cle: str) -> list:
    # convertit le message en valeurs sASCII
    message_ascii = str_en_int(message, len(message))
    # convertit la clé en valeurs ASCII
    cle_ascii = str_en_int(cle, len(message))
    # chiffre les valeurs ASCII
    secret_ascii = [0 for _ in range(len(message))]
    for i in range(len(message_ascii)):
        # opérateur binaire xor
        secret_ascii[i] = message_ascii[i] ^ cle_ascii[i]
    return secret_ascii


def dechiffrement(secret_ascii: list, cle: str) -> str:
    # convertit la clé en valeurs ASCII
    cle_ascii = str_en_int(cle, len(secret_ascii))
    # déchiffre les valeurs ASCII
    message_ascii = [0 for _ in range(len(secret_ascii))]
    for i in range(len(secret_ascii)):
        # opérateur binaire xor
        message_ascii[i] = secret_ascii[i] ^ cle_ascii[i]
    # convertit les valeurs ASCII en lettres
    message = ""
    for lettre_ascii in message_ascii:
        message = message+chr(lettre_ascii)
    return message

if __name__=="__main__":
    cle = "NSI"
    s = chiffrement("BRAVO", cle)
    print(dechiffrement(s, cle))
