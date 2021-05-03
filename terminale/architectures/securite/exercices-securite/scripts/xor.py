#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/05/02 11:28:50
"""


def chiffrer_xor(message: bytes, cle: bytes) -> bytes:
    res = [message[i] ^ cle[i % len(cle)] 
                for i in range(len(message))]
    return bytes(res)

m = "La NSI c'est mââgique!"
cle = "J2B"
m_chiffre = chiffrer_xor(m.encode(), cle.encode())
print(m_chiffre)

m_dechiffre = chiffrer_xor(m_chiffre, cle.encode())
print(m_dechiffre)
print(m_dechiffre.decode())