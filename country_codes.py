# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:35:

@author: ULVI PC
"""

from pygal_maps_world.maps import COUNTRIES
def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
