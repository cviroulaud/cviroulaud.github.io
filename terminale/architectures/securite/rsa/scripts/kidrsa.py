#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/05/06 13:33:48
"""


def creer_nombre(a: int, b: int, a1: int, b1: int) -> dict:
    """
    crée un couple clé privée/publique
    Returns:
        dict: {"publique": (e, n), "privee":(d, n)}
    """
    M = a*b-1
    e = a1*M+a
    d = b1*M+b
    n = (e*d)//M
    return {"publique": (e, n), "privee": (d, n)}


def chiffrer(message: int, publique: tuple) -> int:
    """
    Args:
        message (int)
        publique (tuple): (e, n)

    Returns:
        int: message chiffré
    """
    return (publique[0]*message) % publique[1]


def dechiffrer(message_secret: int, privee: tuple) -> int:
    """
    Args:
        message_secret (int)
        privee (tuple): (d, n)

    Returns:
        int: message déchiffré
    """
    return (privee[0]*message_secret) % privee[1]


cles = creer_nombre(9, 11, 5, 8)
print(cles)
s = chiffrer(538, cles["publique"])
print(s)
e = dechiffrer(s, cles["privee"])
print(e)
