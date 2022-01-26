#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Feb 16 01:34:18 2021

@auteur: Christophe Viroulaud
"""


def utf8(car: str)->str:
    return hex(ord(car))

print(utf8("é"))