#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 20 Mars 2022 18:15
"""
import unittest
from xor import int_en_bin, bin_en_int, renverser


class Test(unittest.TestCase):
    def test_renverser(self):
        self.assertEqual(renverser([1, 2, 3, 3]), [3, 3, 2, 1])
        self.assertEqual(renverser([1, 2, 3]), [3, 2, 1])
        self.assertEqual(renverser([]), [])

    def test_int_bin(self):
        self.assertEqual(int_en_bin(66), [1, 0, 0, 0, 0, 1, 0])
        self.assertEqual(int_en_bin(82), [1, 0, 1, 0, 0, 1, 0])
        self.assertEqual(int_en_bin(65), [1, 0, 0, 0, 0, 0, 1])
        self.assertEqual(int_en_bin(86), [1, 0, 1, 0, 1, 1, 0])
        self.assertEqual(int_en_bin(79), [1, 0, 0, 1, 1, 1, 1])
        self.assertEqual(int_en_bin(78), [1, 0, 0, 1, 1, 1, 0])
        self.assertEqual(int_en_bin(83), [1, 0, 1, 0, 0, 1, 1])
        self.assertEqual(int_en_bin(73), [1, 0, 0, 1, 0, 0, 1])

    def test_bin_int(self):
        self.assertEqual(bin_en_int([1, 0, 0, 0, 0, 1, 0]), 66)
        self.assertEqual(bin_en_int([1, 0, 1, 0, 0, 1, 0]), 82)
        self.assertEqual(bin_en_int([1, 0, 0, 0, 0, 0, 1]), 65)
        self.assertEqual(bin_en_int([1, 0, 1, 0, 1, 1, 0]), 86)
        self.assertEqual(bin_en_int([1, 0, 0, 1, 1, 1, 1]), 79)
        self.assertEqual(bin_en_int([1, 0, 0, 1, 1, 1, 0]), 78)
        self.assertEqual(bin_en_int([1, 0, 1, 0, 0, 1, 1]), 83)
        self.assertEqual(bin_en_int([1, 0, 0, 1, 0, 0, 1]), 73)


if __name__ == "__main__":
    unittest.main()
