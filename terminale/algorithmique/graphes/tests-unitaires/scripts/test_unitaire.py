#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 02 Février 2022 11:45
"""

import unittest
from complet import est_complet
from inverse import f


class Tests(unittest.TestCase):

    def setUp(self):
        self.mat_ok = [[0, 1, 1, 1, 1],
                       [1, 0, 1, 1, 1],
                       [1, 1, 0, 1, 1],
                       [1, 1, 1, 0, 1],
                       [1, 1, 1, 1, 0]]
        self.mat_no = [[1, 1, 1, 1, 1],
                       [1, 0, 1, 1, 1],
                       [1, 1, 0, 1, 1],
                       [1, 1, 1, 0, 1],
                       [1, 1, 1, 1, 0]]

    def test_complet(self):
        self.assertTrue(est_complet(self.mat_ok))
        self.assertFalse(est_complet(self.mat_no))

    def test_inverse(self):
        self.assertTrue(f(1.) == 1.)
        self.assertTrue(f(-1) == -1)

    def test_inverse_erreur(self):
        with self.assertRaises(ZeroDivisionError):
            f(0)


if __name__ == "__main__":
    unittest.main()
