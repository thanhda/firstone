#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:42:52 2017

@author: hien
"""
import pytest
import fun


@pytest.mark.parametrize('n, res', [(3, 9), (2, 4)])
def test_square(n, res):
    print 'Runnin test for square'
    assert fun.square(n) == res


@pytest.mark.parametrize('n, res', [(3, 27), (2, 8)])  
def test_cubic(n, res):
    print 'Running test for cubic'
    assert fun.cubic(n) == res
  

@pytest.mark.parametrize('n, res', [(3, 6), (5, 120), (7, 5040)])
def test_factor(n, res):
    print 'Running test for factor'
    assert fun.factor(n) == res