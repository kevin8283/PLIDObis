from virtual_sensor import virtual_sensor 
import time
import os
import socket
import cbor2 as cbor
    
humidity = virtual_sensor(start=30, variation = 3, min=20, max=80) 
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    humidity_values = []

    time_start = time.time()
    elapsed_time = time.time()

    while elapsed_time - time_start <= 10:
        number_of_values = len(humidity_values)
        print("Collecting humidity values ... (current values obtained: {})".format(number_of_values))

        h = humidity.read_value()
        humidity_values.append(int(h * 100) / 100)
        time.sleep(1)
        os.system('clear')

        elapsed_time = time.time()

    print("10 seconds elapsed, sending {} values".format(len(humidity_values)))
    time.sleep(1)
    s.sendto(cbor.dumps(humidity_values),("127.0.0.1", 33033))
    os.system('clear')
