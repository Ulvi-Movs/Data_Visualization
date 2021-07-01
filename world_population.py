# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:17:19 

@author: ULVI PC
"""

import json
from urllib.request import urlopen
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import RotateStyle



link_data = "https://pkgstore.datahub.io/core/population/population_json/data/315178266aa86b71057e993f98faf886/population_json.json"
data_url = urlopen(link_data )
data = data_url.read().decode()
pop_data = json.loads(data)
cc_populations = {}

for pop_dict in pop_data:
    
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            
        else:
            print( 'ERROR - ' + country_name)
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
    

wm_style = RotateStyle('#336699')
wm = pygal_maps_world.maps.World(style = wm_style)            
wm.title = 'World Population in 2010, by Country'
wm.add ('0 - 10', cc_pops_1)
wm.add ('10m - 1bn', cc_pops_2)
wm.add ('>1bn', cc_pops_3)
wm.render_to_file('world_populations.svg')
