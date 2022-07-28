import socket
import json
from os import system
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 33033))

while True:
    data, addr = s.recvfrom(1500)
    print(json.loads(data.decode()))

    sleep(1)
    system("cls")
