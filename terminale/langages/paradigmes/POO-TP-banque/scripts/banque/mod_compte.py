#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Aug 19 17:28:49 2020

@auteur: Christophe Viroulaud
"""


class Compte:
    """
    Crée un compte

    Paramètre:
        -----
        est_remunere: bool
            initialise le type de compte
    """

    def __init__(self,remunere:bool)->None:
        self.est_remunere=remunere
        self._credit=0

    def credite(self,s:float)->None:
        self._credit+=s

    def debite(self,s:float)->str:
        if self._credit>=s:
            self._credit-=s
            return "Opération effectuée"
        else:
            return "Crédit insuffisant"

    def get_credit(self)->float:
        return self._credit