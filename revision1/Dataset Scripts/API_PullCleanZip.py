# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:23:16 2015

@author: john
"""

import requests
import json
import csv
import pprint
import datetime

#%%
##CELL 1 
###User Inputs
json_location = r'/home/john/Project_5-BLS/test/multiseries3_'
csv_location = r'/home/john/Project_5-BLS/test/csv3_'
tidy_data_location = r'/home/john/Project_5-BLS/test/tidy'
series_list = ['CUURA316SAF','CUURA316SAH',
                'CUURA316SAT', 'CUURA316SAM',
                'CUURA316SAR', 'CUURA316SAE',
                'CUURA316SAG', 'CUURA316SAA',
                'CUURA316SA0']
years_list = [("1982", "1990"), ("1991", "2000"),("2001", "2010"), ("2011", "2015")]
###End User Inputs

headers = {'Content-type': 'application/json'}                

for request in years_list:
    data = json.dumps({"seriesid": series_list,
                         "startyear":request[0], "endyear":request[1]})
    
    response = requests.post('http://api.bls.gov/publicAPI/v1/timeseries/data/',
                             data=data, headers=headers)
    
    json_data = json.loads(response.text)    
    
    with open(json_location + request[0] + "-" + request[1] + ".txt", 'w') as fo:
        json.dump(json_data, fo)
        
#%%
##CELL 2

for request in years_list:
    
    data = {}
    values = []

    with open(json_location + request[0] + "-" + request[1] + ".txt", 'r') as fi:
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
            
    with open(csv_location + request[0] + '-' + request[1] + '.csv', 'w') as fo:
        writer = csv.writer(fo)
        writer.writerow(["seriesID", "date", "value"])
        writer.writerows(export_val)

#%%
#CELL 3
seriesID_dict = {'CUURA316SAT' : "Transportation",
            'CUURA316SAR' : "Recreation",
            'CUURA316SAF' : "Food & Bev.",
            'CUURA316SAE' : "Education & Com.",
            'CUURA316SAG' : "Other Goods & Serv.",
            'CUURA316SAA' : "Apparel",
            'CUURA316SAM' : "Medical",
            'CUURA316SAH' : "Housing",
            'CUURA316SA0' : "All Items"}
            
combined = []
export_zip = []
                      
for request in years_list:
    with open(csv_location + request[0] + '-' + request[1] + '.csv', 'r') as fi:
        reader = csv.reader(fi, delimiter = ',')
        for row in reader:
            combined.append(row)

for val in combined:
    if val[0] == "seriesID":
        continue
    interm_val = []
    interm_val.append(seriesID_dict.get(val[0]))
    interm_val.append(val[0])
    timestring = val[1]
    timeobject = datetime.datetime.strptime(timestring, "%B-%Y")
    interm_val.append(timeobject)
    interm_val.append(val[2])
    export_zip.append(interm_val)

export_zip = sorted(export_zip, key = lambda export_zip: (export_zip[0], export_zip[1]))

for val in export_zip:
    val[2] = val[2].strftime("%B-%Y")        
                
pprint.pprint(export_zip)

with open(tidy_data_location + years_list[0][0] + '-' + years_list[-1][1] + '.csv', 'w') as fo:
    writer = csv.writer(fo)
    writer.writerow(["descrip", "seriesID", "date", "cpi-value"])
    writer.writerows(export_zip)        
                      