#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 05 Octobre 2021 22:17
"""

from est_pair import est_pair
import unittest


class Tests(unittest.TestCase):
    def test_est_pair(self):
        self.assertTrue(est_pair(4), msg="Erreur si x est pair")
        self.assertFalse(est_pair(5), msg="Erreur si x est impair")



if __name__ == "__main__":
    unittest.main()
