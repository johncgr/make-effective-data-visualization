# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:21:12 2015

@author: john
"""

import requests
import json

headers = {'Content-type': 'application/json'}

data = json.dumps({"seriesid": ['CUURA316SAF','CUURA316SAH',
                                'CUURA316SAT', 'CUURA316SAM',
                                'CUURA316SAR', 'CUURA316SAE',
                                'CUURA316SAG', 'CUURA316SAA'],
                     "startyear":"2011", "endyear":"2015"})

response = requests.post('http://api.bls.gov/publicAPI/v1/timeseries/data/',
                         data=data, headers=headers)

json_data = json.loads(response.text)

with open(r'/home/john/Project_5-BLS/bls_json_multiseries_11-15.txt', 'w') as fo:
    json.dump(json_data, fo)

