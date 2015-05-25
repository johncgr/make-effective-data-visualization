# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:52:19 2015

@author: john
"""
import csv
import pprint
import datetime

seriesID_dict = {'CUURA316SAT' : "Transportation",
            'CUURA316SAR' : "Recreation",
            'CUURA316SAF' : "Food & Bev.",
            'CUURA316SAE' : "Education & Com.",
            'CUURA316SAG' : "Other Goods & Serv.",
            'CUURA316SAA' : "Apparel",
            'CUURA316SAM' : "Medical",
            'CUURA316SAH' : "Housing" }

file1 = r'/home/john/Project_5-BLS/bls_tidy_multiseries82-90.csv'
file2 = r'/home/john/Project_5-BLS/bls_tidy_multiseries91-00.csv'
file3 =r'/home/john/Project_5-BLS/bls_tidy_multiseries01-10.csv'
file4 = r'/home/john/Project_5-BLS/bls_tidy_multiseries11-15.csv'

combined = []
export_val = []

with open(file1, 'r') as f1:
    reader = csv.reader(f1, delimiter=",")
    for row in reader:
        combined.append(row)

with open(file2, 'r') as f1:
    reader = csv.reader(f1, delimiter=",")
    for row in reader:
        combined.append(row)
        
with open(file3, 'r') as f1:
    reader = csv.reader(f1, delimiter=",")
    for row in reader:
        combined.append(row)
        
with open(file4, 'r') as f1:
    reader = csv.reader(f1, delimiter=",")
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
    export_val.append(interm_val)

export_val = sorted(export_val, key = lambda export_val: (export_val[0], export_val[1]))

for val in export_val:
    val[2] = val[2].strftime("%B-%Y")        
                
pprint.pprint(export_val)

with open(r'/home/john/Project_5-BLS/bls_tidy_multiseries2_82-2015.csv', 'w') as fo:
    writer = csv.writer(fo)
    writer.writerow(["descrip", "seriesID", "date", "cpi-value"])
    writer.writerows(export_val)        