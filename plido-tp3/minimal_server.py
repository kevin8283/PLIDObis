import socket
import os
import binascii
import time
import cbor2 as cbor

os.system("clear")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 33033))

temperature_values = []
pressure_values = []
humidity_values = []

def calculate_average(array):
    sum = 0
    for value in array:
        sum += value
   
    return sum / len(array)

while True:
    data, addr = s.recvfrom(1500)
   
    captor_values = cbor.loads(data)

    temperature_values.append(captor_values[0] / 100)
    pressure_values.append(captor_values[1] / 100 )
    humidity_values.append(captor_values[2] / 100 )

    avg_temp = calculate_average(temperature_values)
    avg_press = calculate_average(pressure_values)
    avg_hum = calculate_average(humidity_values)

    print("Average values from captor: ")
    print("")
    print("Temperature: ", avg_temp)
    print("Pressure: ", avg_press)
    print("Humidity: ", avg_hum)

    time.sleep(2)
    os.system('clear')
