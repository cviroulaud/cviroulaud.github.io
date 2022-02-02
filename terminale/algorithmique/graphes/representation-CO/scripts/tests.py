#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 01 Février 2022 22:46
"""
import unittest
from conversion import mat_to_dic


class Tests(unittest.TestCase):

    def setUp(self):
        self.mat = [[0, 1, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 1, 0, 0, 1],
                    [0, 0, 1, 0, 0, 0],
                    [1, 0, 0, 1, 0, 0]]
        self.dic = {'A': ['B', 'C', 'F'], 'B': ['A'], 'C': [
            'A', 'D', 'E'], 'D': ['C', 'F'], 'E': ['C'], 'F': ['A', 'D']}

    def test_mat_to_dic(self):
        self.assertTrue(mat_to_dic(self.mat) == self.dic)


if __name__ == "__main__":
    unittest.main()
