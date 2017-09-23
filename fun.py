#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:50:20 2017

@author: hien
"""

def square(n):
    return n*n

def cubic(n):
    return n*n*n

def factor(n):
    if n == 0: return 1
    else:
        return n*factor(n - 1)
    
