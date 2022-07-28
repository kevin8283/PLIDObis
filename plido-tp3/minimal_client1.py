from virtual_sensor import virtual_sensor 
import time
import socket
import json

temperature = virtual_sensor(start=20, variation = 0.1)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    t = temperature.read_value()
    serialized_data = {
        "temperature": t
    }
    
    data = json.dumps(serialized_data).encode()

    s.sendto (data, ("127.0.0.1", 33033))
    time.sleep(1)

