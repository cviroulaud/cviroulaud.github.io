#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 20 Mars 2022 18:15
"""
import unittest
from xor import appliquer_xor


class Test(unittest.TestCase):
    def setUp(self):
        self.entree_bin = [[1, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 1, 0], [
            1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 1, 1]]
        self.cle_bin = [[1, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1, 1], [
            1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1, 1]]
        self.sortie_bin = [[0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1], [
            0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0]]

    def test_appliquer_xor(self):
        self.assertEqual(appliquer_xor(
            self.entree_bin, self.cle_bin), self.sortie_bin)


if __name__ == "__main__":
    unittest.main()
