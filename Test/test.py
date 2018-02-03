# -*- coding: utf-8 -*-
'''
Created on 2016-11-30

@author: Polly

'''

import requests

url = 'http://192.168.56.103:8000'
options = [
	'/getDirectoryBrowserInfo/',
	'/directoryAddition/',
]

payload = {'currentPath': '/home/polly'}
r = requests.post(url+options[0], data=payload)
print r.text