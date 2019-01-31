#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search4.py

import socket
from urllib.parse import quote_plus
import ssl
from api_util import load_key

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false&key={} HTTP/1.1\r\n\
Host: maps.google.com:443\r\n\
User-Agent: search4.py (Foundations of Python Network Programming)\r\n\
Connection: close\r\n\
\r\n\
"""

def geocode(address):
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose)
    raw_sock = socket.socket()
    raw_sock.connect(('maps.google.com', 443))
    ssl_sock = context.wrap_socket(raw_sock, server_hostname='maps.google.com')
    request = request_text.format(quote_plus(address), load_key())
    ssl_sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = ssl_sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
