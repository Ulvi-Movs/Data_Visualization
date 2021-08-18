# -*- coding: utf-8 -*-
"""
Created on Thu May 20

@author: ULVI PC
"""

import matplotlib.pyplot as plt

imput_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(imput_values, squares, linewidth = 5)
plt.title("Square Numbers")
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.tick_params(axis = "both", labelsize = 14)
plt.show()
