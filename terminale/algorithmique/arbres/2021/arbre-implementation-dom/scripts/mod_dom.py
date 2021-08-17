#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan 15 14:13:26 2021

@auteur: Christophe Viroulaud
"""

# non finalisé!!!
class Noeud:
    def __init__(self, v: str, f: list)->None:
        self.valeur = v
        self.fils = f

    def __str__(self):
        res = self.valeur + "\n\t"
        for f in self.fils:
            res += f.valeur + "\n\t"
        return res

class Arbre:
    def __init__(self):
        # faire entrées manuelles
        self.dom = Noeud("html", [Noeud("head", [Noeud("meta", [Noeud("charset", [Noeud("utf-8", [])])]),
                                    Noeud("title", [Noeud("text", [Noeud("Présentation NSI seconde", [])])])]),
                     Noeud("body", [Noeud("p", [Noeud("text", [Noeud("La NSI est trop cool!!", [])])]),
                                    Noeud("ul", [Noeud("li", [Noeud("text", [Noeud("Programmation", [])])]),
                                                 Noeud("li", [Noeud("text", [Noeud("Algorithmie", [])])]),
                                                 Noeud("li", [Noeud("text", [Noeud("Architecture machine", [])])]),
                                                 Noeud("li", [Noeud("text", [Noeud("Langages du web", [])])])]),
                                    Noeud("a", [Noeud("href", [Noeud("https://cviroulaud.github.io", [])]),
                                                Noeud("text", [Noeud("Les cours de NSI", [])])]),
                                    Noeud("img", [Noeud("src", [Noeud("images/nsi.png", [])])])])])

    def taille(self)->int:  # erreur: il faut un appel principal
        """
        renvoie le nombre d'éléments de dom
        """
        t = 1
        for f in self.dom.fils:
            t += self.taille(f)
        return t

    def get_elements_by_tagname_rec(self, tag: str, arbre: Noeud, res: list)->list:
        """
        récupère la liste des noeuds de 'e' dans 'arbre'
        """
        if arbre.valeur == tag:
            res.append(arbre)
        for f in arbre.fils:
            self.get_elements_by_tagname_rec(tag, f, res)
        return res

    def get_elements_by_tagname(self, tag: str)->list:
        """
        appel principal de get_elements
        """
        return self.get_elements_by_tagname_rec(tag, self.dom, [])

dom = Arbre()

for n in dom.get_elements_by_tagname("head"):
    print(n)

for n in dom.get_elements_by_tagname("text"):
    print(n.fils[0].valeur)