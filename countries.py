# -*- coding: utf-8 -*-
"""
Created on Thu May 

@author: ULVI P
"""

from pygal_maps_world.maps import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
