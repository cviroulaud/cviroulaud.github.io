#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Aug 19 15:02:21 2020

@auteur: Christophe Viroulaud
"""

from mod_compte import Compte

class Client:
    """
    Crée un client

    Paramètres
        -----
        nom: str
            nom du client
    """

    def __init__(self,n:str)->None:
        self.nom=n
        self._comptes={}

    def ouvre_compte(self,remunere:bool,i:int)->None:
        self._comptes[i]=Compte(remunere)

    def ferme_compte(self,i:int)->str:
        if self._comptes.has_key(i):
            del self._comptes[i]
            return "Le compte est supprimé."
        else:
            return "Ce compte n'existe pas."

    """
    def ferme_compte(self,i:int)->str:
        c=self._comptes.get(i)
        if c:
            del self._comptes[i]
            return "Le compte est supprimé."
        else:
            return "Ce compte n'existe pas."
    """

    """
    def ferme_compte(self,i:int)->str:
        try:
            del self._comptes[i]
            return "Le compte est supprimé."
        except keyError:
            return "Ce compte n'existe pas."
    """

    def get_comptes(self)->dict:
        return self._comptes