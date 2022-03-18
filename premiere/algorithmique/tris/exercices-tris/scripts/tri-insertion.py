#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/07 22:59:29
"""

from random import randint


def tri_insertion(tab: list) -> list:
    """
    renvoie une copie triée de tab
    """
    tab_trie = []
    for i in range(len(tab)):
        # mémoriser
        en_cours = tab[i]
        tab_trie.append(en_cours)
        pos = len(tab_trie)-1
        # décaler
        while pos > 0 and en_cours < tab_trie[pos-1]:
            tab_trie[pos] = tab_trie[pos-1]
            pos = pos-1
        # insérer
        tab_trie[pos] = en_cours
    return tab_trie


t = [randint(0, 100) for _ in range(10)]
print(tri_insertion(t))
print(t)
