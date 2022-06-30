import socket
import os
import binascii
import time
import cbor2 as cbor

os.system("clear")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 33033))

while True:
    data, addr = s.recvfrom(1500)
   
    humidity_values = cbor.loads(data)

    print(humidity_values)
