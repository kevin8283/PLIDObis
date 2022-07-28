import socket
import json

from time import sleep
from lib.bmp180 import BMP180
from machine import I2C, Pin as pin

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

NB_ELEMENT = 30
t_history = []

bus = I2C(scl = pin(5), sda = pin(4))
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

while True:

    t = int(bmp180.temperature)

    # No more room to store value, send it.
    if len(t_history) == 0:
        t_history = [t]

    elif len(t_history) >= NB_ELEMENT:
        print ("send")
        server.sendto(json.dumps(t_history), ("192.168.137.1", 33033))
        t_history = [t]

    else:
        t_history.append(t)

    print(len(t_history), len(json.dumps(t_history)), t_history)

    sleep(2)