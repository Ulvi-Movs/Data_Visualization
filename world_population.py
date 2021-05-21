# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:17:19 2021

@author: ULVI PC
"""

import json
from urllib.request import urlopen

link_data = "https://pkgstore.datahub.io/core/population/population_json/data/315178266aa86b71057e993f98faf886/population_json.json"
data_url = urlopen(link_data )
data = data_url.read().decode()
pop_data = json.loads(data)

for pop_dict in pop_data:

    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ": " + str(population))