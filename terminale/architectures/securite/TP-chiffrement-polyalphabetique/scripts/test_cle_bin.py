#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 20 Mars 2022 18:15
"""
import unittest
from tp_chiffrement import creer_cle_bin


class Test(unittest.TestCase):
    def test_cle_bin(self):
        self.assertEqual(creer_cle_bin("NSI", 5), [[1, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1, 1], [
            1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1, 1]])


if __name__ == "__main__":
    unittest.main()
