#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 22 Janvier 2022 11:53
"""


class Adresse:

    def __init__(self, adresse: str):
        self.adresse = ...

    def liste_octet(self) -> list:
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self) -> bool:
        """renvoie True si l'adresse IP est une adresse
           réservée, False sinon"""
        return ... or ...

    def adresse_suivante(self) -> object:
        """renvoie un objet de Adresse avec l'adresse 
           IP qui suit l’adresse self
           si elle existe et False sinon"""
        dernier_octet = ...
        if ... < 254:
            octet_nouveau = ... + ...
            return Adresse('192.168.0.' + ...)
        else:
            return None


adresse1 = Adresse("192.168.0.1")
adresse2 = Adresse("192.168.0.2")
adresse3 = Adresse("192.168.0.0")
print(adresse1.est_reservee())
print(adresse3.est_reservee())
print(adresse2.adresse_suivante().adresse)