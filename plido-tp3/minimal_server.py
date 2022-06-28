import socket
import os
import binascii
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 33033))

temperature_values = []

def calculate_average(array):
    sum = 0
    for value in array:
        sum += value
   
    return sum / len(array)

while True:
    data, addr = s.recvfrom(1500)
    temperature = float(data.decode())
    temperature_values.append(temperature)

    print("Average temperature :", calculate_average(temperature_values))
    time.sleep(2)
    os.system('clear')
