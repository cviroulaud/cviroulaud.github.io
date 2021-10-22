#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 21 Octobre 2021 22:19
"""
from threading import Thread
from time import sleep


def f1():
    for _ in range(5):
        print("appel 1")
        sleep(0.0001)


def f2():
    for _ in range(5):
        print("appel 2")
        sleep(0.0001)


p1 = Thread(target=f1)
p2 = Thread(target=f2)
p1.start()
p2.start()
"""
pour forcer le programme à
attendre la fin des thread
"""
p1.join()
p2.join()
