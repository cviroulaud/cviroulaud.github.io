#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Aug 21 10:10:53 2020

@auteur: Christophe Viroulaud
"""


class Loto:

    def __init__(self,num,c):
        self.numeros=num
        self.complementaire=c

    def __contains__(self,n):
        return n in self.numeros

    def __str__(self):
        return str(self.complementaire)

l=Loto([1,2,3,4,5,6],7)
print(l)
print(5 in l)