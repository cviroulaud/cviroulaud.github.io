#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 19 Octobre 2021 13:17
"""


from pile import Pile


def polonaise(chaine: str) -> int:
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
