# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:32:55 2020

@author: SABARISH
"""

def MaxReducedString(s):
    res = ''
    i = 0
    while i < len(s):
        if i + 1 == len(s) or s[i + 1] != s[i]:
            res += s[i]
        else:
            i += 1
        i += 1
    return res
def superReducedString(origin):
    res = MaxReducedString(origin)
    while res != origin:
        res, origin = MaxReducedString(res), res
    return res or 'Empty String'


superReducedString("abccddd")