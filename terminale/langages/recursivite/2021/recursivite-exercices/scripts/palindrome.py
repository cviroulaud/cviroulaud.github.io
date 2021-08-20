#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:40:51 2020

@author: Christophe Viroulaud
"""

def palindrome(s):
    if len(s)<2:
        return True
    elif not(s[0]==s[-1]):
        return False
    else:
        return palindrome(s[1:-1])
    
print(palindrome("ressasser"))
print(palindrome("ressadsser"))