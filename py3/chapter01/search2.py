#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search2.py

import requests
from api_util import load_key

def geocode(address):
    parameters = {'address': address, 'sensor': 'false', 'key': load_key()}
    base = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
