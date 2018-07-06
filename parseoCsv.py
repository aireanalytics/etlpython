# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 18:58:13 2018

@author: fpena
"""
import json
import pandas
from pandas.io.json import json_normalize

#estaciones = ['3100B','3110C','3191E','3200','3129','3194U','3196','3195','3266A','2462','3338','3111D','3175']
estaciones = ['3100B']
df = pandas.DataFrame([])
for estacion in estaciones:
    fichero = estacion + 'data.json'
    print (fichero)
    with open(fichero, mode='r') as f:
       json_data = json.loads(f.read())
       data_norm = json_normalize(json_data)
       df.append(data_norm, ignore_index=True)
       print (df)