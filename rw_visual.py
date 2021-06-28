# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:26:06 

@author: ULVI PC
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(dpi=128, figsize = (10,6))
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_number, cmap = plt.cm.Blues, edgecolor='none', s=1)
    plt.scatter(0, 0, c = 'green', edgecolor = 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolor = 'none', s = 100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_runing = input("Make another walk? (y/n):")
    if keep_runing == 'n':
        break
