#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 01:38:51 2026

@author: E131046
"""

import numpy as np

def phase(t):
    p= 1 + 3 * t + (1/2) * 0.04 * t**2
    return p
def phase_freq(t):
    p = 100 + 3 * t + (1/2) * 40 * t**2
    return p

def gw(t):
    g = 1 + np.sin(phase(t))
    return g

step = 8

x = np.arange(0,step*np.pi*2)

x=[]
for i in range(step):
    x.append(i/2*np.pi)

x = np.asarray(x)

phase(x)
