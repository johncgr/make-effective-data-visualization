# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:40:27 2015

@author: john
"""
import json
import csv
import pprint
import datetime

data = {}

values = []

with open(r'/home/john/Project_5-BLS/bls_json_multiseries_82-90.txt', 'r') as fi:
    data = json.load(fi)
    
#to make lists
for series in data['Results']['series']:
    series_id = series['seriesID']
    for items in series['data']:
        year = items['year']
        month = items['periodName']
        value = items['value']
        values.append([year, month, value, series_id])
#end list making

export_val = []
timestring = ""
timeobject = ""

for val in values:
        interm_val = []
        interm_val.append(val[3])
        timestring = (val[1] + "-" + val[0])
        timeobject = datetime.datetime.strptime(timestring, "%B-%Y")
        interm_val.append(timeobject)
        interm_val.append(val[2])
        export_val.append(interm_val)

export_val = sorted(export_val, key = lambda export_val: (export_val[0], export_val[1]))

for val in export_val:
    val[1] = val[1].strftime("%B-%Y")

pprint.pprint(export_val)
        
with open(r'/home/john/Project_5-BLS/bls_tidy_multiseries82-90.csv', 'w') as fo:
    writer = csv.writer(fo)
    writer.writerow(["seriesID", "date", "value"])
    writer.writerows(export_val)

    
        