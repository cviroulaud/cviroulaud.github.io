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


def taille(dom: Noeud)->int:
    """
    renvoie le nombre d'éléments de dom
    """
    t = 1
    for f in dom.fils:
        t += taille(f)
    return t

print("nombre d'éléments: ", taille(dom))

def get_elements_by_tagname(tag: str, arbre: Noeud, res: list)->list:
    """
    récupère la liste des noeuds de 'e' dans 'arbre'
    """
    if arbre.valeur == tag:
        res.append(arbre)
    for f in arbre.fils:
        get_elements_by_tagname(tag, f, res)
    return res

for n in get_elements_by_tagname("head", dom, []):
    print(n)

for n in get_elements_by_tagname("text", dom, []):
    print(n.fils[0].valeur)

"""
variante avec gestion effet de bord
"""
def get_elements_by_tagname2(tag: str, arbre: Noeud, res: list = None)->list:
    # gestion de l'effet de bord potentiel
    if res is None:
        res = []

    if arbre.valeur == tag:
        res.append(arbre)
    for f in arbre.fils:
        get_elements_by_tagname(tag, f, res)
    return res

for n in get_elements_by_tagname2("head", dom):
    print(n)

for n in get_elements_by_tagname2("text", dom):
    print(n.fils[0].valeur)


"""
variante avec fonction interne
pour englober la liste vide 'res'
et éviter effet de bord avec list() en valeur défaut
"""
def get_elements_by_tagname3(tag: str, arbre: Noeud):
    def get_elements_interne(tag: str, arbre: Noeud, res: list)->list:
        if arbre.valeur == tag:
            res.append(arbre)
        for f in arbre.fils:
            get_elements_by_tagname(tag, f, res)
        return res

    return get_elements_interne(tag, arbre, [])

for n in get_elements_by_tagname3("head", dom):
    print(n)

for n in get_elements_by_tagname3("text", dom):
    print(n.fils[0].valeur)
