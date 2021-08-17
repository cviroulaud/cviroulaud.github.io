#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan 15 14:13:26 2021

@auteur: Christophe Viroulaud
"""


class Noeud:
    def __init__(self, v: str, f: list)->None:
        self.valeur = v
        self.fils = f

    def __str__(self):
        res = self.valeur + "\n\t"
        for f in self.fils:
            res += f.valeur + "\n\t"
        return res

dom = Noeud("html", [Noeud("head", [Noeud("meta", [Noeud("charset", [Noeud("utf-8", [])])]),
                                    Noeud("title", [Noeud("text", [Noeud("Présentation NSI seconde", [])])])]),
                     Noeud("body", [Noeud("p", [Noeud("text", [Noeud("La NSI est trop cool!!", [])])]),
                                    Noeud("ul", [Noeud("li", [Noeud("text", [Noeud("Programmation", [])])]),
                                                 Noeud("li", [Noeud("text", [Noeud("Algorithmie", [])])]),
                                                 Noeud("li", [Noeud("text", [Noeud("Architecture machine", [])])]),
                                                 Noeud("li", [Noeud("text", [Noeud("Langages du web", [])])])]),
                                    Noeud("a", [Noeud("href", [Noeud("https://cviroulaud.github.io", [])]),
                                                Noeud("text", [Noeud("Les cours de NSI", [])])]),
                                    Noeud("img", [Noeud("src", [Noeud("images/nsi.png", [])])])])])

