import socket
import lib.kpn_senml.cbor_encoder as cbor

from time import sleep
from lib.bmp180 import BMP180
from machine import I2C, Pin as pin

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

NB_ELEMENT = 30
bus = I2C(scl = pin(5), sda = pin(4))
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

t_history = []

while True:
    temp = int(bmp180.temperature)
    
    if len(t_history) == 0:
        t_history = [temp]

    elif len(t_history) >= NB_ELEMENT:
        print ("Sending values to server")
        server.sendto(cbor.dumps(t_history), ("192.168.137.1", 33033))
        t_history = [temp]

    else:
        t_history.append(temp - prev)

    prev = temp
    
    sleep(2)