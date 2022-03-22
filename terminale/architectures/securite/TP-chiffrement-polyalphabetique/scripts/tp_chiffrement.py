#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 20 Mars 2022 16:09
"""


def renverser(tab: list) -> list:
    """
    renverse un tableau
    """
    l = len(tab)
    res = [0 for _ in range(l)]
    for i in range(l):
        res[l-1-i] = tab[i]
    return res


def int_en_bin(nb: int) -> list:
    """
    Convertit un entier en sa représentation binaire
    """
    q = nb
    r = []
    while q > 0:
        r.append(q % 2)
        q = q//2

    return renverser(r)


def bin_en_int(paquet: list) -> int:
    """
    Convertit un paquet de bits en entier
    """
    entier = 0
    for i in range(len(paquet)):
        entier += int(paquet[i])*2**(len(paquet)-1-i)
    return entier


def xor(x: int, y: int) -> int:
    """
    applique la porte x xor y
    """
    if x == 0:
        if y == 0:
            return 0
        else:
            return 1
    else:
        if y == 0:
            return 1
        else:
            return 0


def creer_cle_bin(cle: str, taille: int) -> list:
    """
    crée la version binaire de la clé, de la taille
    du message à chiffrer
    """
    cle_bin = []
    for i in range(taille):
        # si dépasse taille de la clé, revient à 0
        lettre = cle[i % len(cle)]
        cle_bin.append(int_en_bin(ord(lettre)))
    return cle_bin


def appliquer_xor(entree_bin: list, cle_bin: list) -> list:
    """
    applique xor sur chaque bit des tableaux de entree_bin

    Args:
        entree_bin (list): tableau de tableau
        cle_bin (list): tableau de tableau

    Returns:
        list: tableau de tableau
    """
    sortie_bin = [[0 for _ in range(len(entree_bin[0]))]
                  for _ in range(len(entree_bin))]
    for i in range(len(entree_bin)):
        for j in range(len(entree_bin[0])):
            sortie_bin[i][j] = xor(entree_bin[i][j], cle_bin[i][j])
    return sortie_bin


def chiffrement(message: str, cle: str) -> list:
    # convertit le message en binaire
    message_bin = []
    for lettre in message:
        message_bin.append(int_en_bin(ord(lettre)))
    # convertit la clé en binaire
    cle_bin = creer_cle_bin(cle, len(message))
    # chiffre le message
    secret_bin = appliquer_xor(message_bin, cle_bin)
    return secret_bin


def dechiffrement(secret_bin: list, cle: str) -> str:
    # convertit la clé en binaire
    cle_bin = creer_cle_bin(cle, len(secret_bin))
    # déchiffre le secret binaire
    message_bin = appliquer_xor(secret_bin, cle_bin)
    # convertit le message binaire en caractères
    message = ""
    for lettre_bin in message_bin:
        message = message+chr(bin_en_int(lettre_bin))
    return message


if __name__ == "__main__":
    print(f"0 xor 0 -> {xor(0, 0)}")
    print(f"0 xor 1 -> {xor(0, 1)}")
    print(f"1 xor 0 -> {xor(1, 0)}")
    print(f"1 xor 1 -> {xor(1, 1)}")

    cle = "NSI"
    s = chiffrement("BRAVO", cle)
    print(dechiffrement(s, cle))
