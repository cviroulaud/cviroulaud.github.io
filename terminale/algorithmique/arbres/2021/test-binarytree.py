#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Jan 19 09:18:27 2021

@auteur: Christophe Viroulaud
"""


from binarytree import Node

# Créer un arbre
arbre = Node(20)
arbre.left = Node(5)
arbre.right = Node(25)
arbre.left.left = Node(3)
arbre.left.right = Node(12)
arbre.right.left = Node(21)

print(arbre)