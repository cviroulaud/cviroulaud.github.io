#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Aug 18 16:31:08 2020

@auteur: Christophe Viroulaud
"""


class Distance_us:
    """
    Définit une distance US en pieds et pouces

    Paramètres
        ----------
        feet : int
            pieds.
        inch : int
            pouces.
    """

    def __init__(self, feet, inch):
        self.pied=feet
        self.pouce=inch

    def __str__(self):
        """
        Renvoie une chaîne décrivant l'objet.
        """
        return "La distance est de {} pieds et {} pouces.".format(self.pied,self.pouce)

    def __eq__(self, other):
        """
        Compare 2 objets. Cette méthode redéfinit ==.
        """
        d1=self.pied*12+self.pouce
        d2=other.pied*12+other.pouce
        if d1==d2:
            return "Les distances sont égales."
        else:
            return "Les distances sont différentes."

    def convertir(self):
        """
        Convertit en mètres la distance US.
        1 pied = 0.3048m
        """
        return self.pied*0.3048+self.pouce*0.3048/12

if __name__=="__main__":
    d1=Distance_us(6,5)
    d2=Distance_us(5,17)
    print(d1==d2)
    d3=Distance_us(3, 8)
    print(d3.convertir())
    help(Distance_us)