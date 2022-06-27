from pymodbus.client.sync import ModbusTcpClient
import time
import os

# open connection with gateway at the specified address
client = ModbusTcpClient('192.168.3.36', port=5020)
client.connect()

def get_water_level():
    result = client.read_input_registers(unit=28, address=0x00ff, count=1)

    return result.registers[0] / 100

def set_pump_speed(speed):
    client.write_register(unit=48, address=0x0200, count=1, value=speed)

while True:
    water_level = get_water_level()
    print("Water level: ", water_level, " %")

    if water_level < 95:
        set_pump_speed(20)
    
    elif water_level >= 95 and water_level <= 98:
        set_pump_speed(5)

    elif water_level > 98:
        set_pump_speed(0)
    
    time.sleep(0.25)
    os.system("clear")


