# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 19:47:21 2020

@author: khwaja
"""


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'CRIM':0.00632,'ZN':18,'CHAS':0,'NOX':0.538,'RM':6.575,'AGE':65.2, 'DIS':4.090, 'RAD':1.0, 'PT_RATIO':15.3, 'LSTAT':4.98 })

print(r.json())