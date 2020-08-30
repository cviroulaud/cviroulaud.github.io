#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Aug 19 14:56:25 2020

@auteur: Christophe Viroulaud
"""

from mod_client import Client

class Banque:
    """
    Crée la banque

    Paramètres
        -----
        nom: str
            nom de la banque
        taux: float
            taux de rémunération
    """

    def __init__(self, n, t):
        self.nom=n
        self.taux=t
        self._clients=[]
        self._id_libre=1

    def cree_client(self, n:str)->None:
        client=Client(n)
        #ouvre le compte courant par défaut
        client.ouvre_compte(False,self._id_libre)
        #incrémente le compteur pour n'avoir que des id uniques
        self._id_libre+=1
        #ouvre le compte rémunéré
        client.ouvre_compte(True,self._id_libre)
        #incrémente le compteur pour n'avoir que des id uniques
        self._id_libre+=1
        self._clients.append(client)

    def trouve_client(self, n:str)->Client:
        for client in self._clients:
            if client.nom == n:
                return client
        return False

    def remunere(self)->None:
        for client in self._clients:
            for compte in client.get_comptes().values():
                if compte.est_remunere:
                    credit=compte.get_credit()
                    compte.debite(credit)
                    credit*=self.taux
                    compte.credite(credit)