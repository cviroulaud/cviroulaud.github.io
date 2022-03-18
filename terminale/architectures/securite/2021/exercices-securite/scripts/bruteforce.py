#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/05/07 15:21:47
"""

from xor import chiffrer_xor
import time


def compare_fin(message: bytes, fin: bytes) -> bool:
    """
    compare la fin de 'message' à 'fin'
    NB: on compare ici des octets; len(bytes) renvoie un
    nombre d'octets (cela reste équivalent à comparer des
    lettres ASCII)
    """
    return message[-len(fin):] == fin


def compare_fin2(message: bytes, fin: bytes) -> bool:
    i_message = len(message)-1
    i_fin = len(fin)-1
    while i_fin >= 0 and message[i_message] == fin[i_fin]:
        i_message -= 1
        i_fin -= 1
    return i_fin < 0


def bruteforce(secret: bytes) -> tuple:
    """
    Teste toutes les combinaisons de 3 lettres minuscules
    pour trouver la clé
    """
    for l1 in range(97, 123):
        for l2 in range(97, 123):
            for l3 in range(97, 123):
                # création de la clé
                cle = chr(l1)+chr(l2)+chr(l3)
                # tentative de décryptage avec cette clé
                message = chiffrer_xor(secret, cle.encode())
                # comparaison de la fin du message
                if compare_fin(message, "Tof!".encode()):
                    return (message.decode(), cle)
    return "Message non décrypté!"


message_secret = b'>\x04\tR\xa2\xd3\x1e\xa2\xd2\x04\x04\tR\x05\x1fR\x15\x1f\x00\x0c\x13\x1c\x00\x16\x17A\t\x1d\x0f\x0eR\x15\x08\x1d\x11Z\x10\x00\x16\xb1\xc9\x00\x17\x12[R5\x15\x14@'
debut = time.time()
message_decrypte = bruteforce(message_secret)
fin = time.time()
print(message_decrypte)
print(fin-debut)

def bruteforce2(secret: bytes) -> tuple:
    """
    Teste toutes les combinaisons de 4 lettres minuscules
    pour trouver la clé
    """
    for l1 in range(97, 123):
        for l2 in range(97, 123):
            for l3 in range(97, 123):
                for l4 in range(97, 123):
                    # création de la clé
                    cle = chr(l1)+chr(l2)+chr(l3)+chr(l4)
                    # tentative de décryptage avec cette clé
                    message = chiffrer_xor(secret, cle.encode())
                    # comparaison de la fin du message
                    if compare_fin(message, "Tof!".encode()):
                        return (message.decode(), cle)
    return "Message non décrypté!"

message_secret = b'8\x00\x01M\xb7\xcc\x1e\xae\xdc\x13\x17\x1eT\x01\x17M\x00\x00\x00\x00\x1d\x0b\x13\x01\x11E\x01\x02\x1a\x11R\x19\x06\n\x02M\x16\x04\x1e\xae\xdc\x1f\x17\x1eUE&\x02\x12D'
debut = time.time()
message_decrypte = bruteforce2(message_secret)
fin = time.time()
print(message_decrypte)
print(fin-debut)
print("noël".encode())