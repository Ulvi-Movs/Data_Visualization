# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:30:12 2021

@author: ULVI PC
"""

from pygal_maps_world.maps import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])