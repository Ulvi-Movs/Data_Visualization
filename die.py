# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:33:07 2021

@author: ULVI PC
"""

from random import randint
class Die():
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
        
    def roll(self):
        return randint(1, self.num_sides)
    