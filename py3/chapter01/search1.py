#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search1.py

from pygeocoder import Geocoder
from api_util import load_key

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    print(Geocoder(load_key()).geocode(address)[0].coordinates)
