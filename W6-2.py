#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:57:30 2017

@author: faye
"""

import urllib
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    
    address = raw_input('Enter location: ')
    print '=========================='
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode({'sensor': False, 'address': address})

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read().decode()
    print 'Retrieved', len(data), 'characters'

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        #print(data)
        continue

    print(json.dumps(js, indent=4))

    place_id = js["results"][0]["place_id"]
    print 'place_id: ', place_id