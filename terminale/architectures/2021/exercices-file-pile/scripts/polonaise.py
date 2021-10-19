#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 16 14:35:26 2020

@auteur: Christophe Viroulaud
"""


from mod_pile import Pile

def polonaise(chaine: str)->int:
    p = Pile()
    for e in chaine.split():
        if e == "+" or e == "*":
            val1 = p.depiler()
            val2 = p.depiler()
            if e == "+":
                p.empiler(val1+val2)
            else:
                p.empiler(val1*val2)
        else:
            p.empiler(int(e))

    return p.depiler()

chaine = "1 2 3 * + 4 *"
print(polonaise(chaine))