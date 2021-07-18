# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:54

@author: ULVI PC
"""

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()

wm.title = 'Populations of countries in North America'
wm.add('North America', { 'co': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')
