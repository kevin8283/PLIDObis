from pymodbus.client.sync import ModbusTcpClient
import time
import os

client = ModbusTcpClient("192.168.3.36", port=5020)

def clear_output():
    os.system("clear")

while True:
    result = client.read_input_registers(address=0x00ff, count=1, unit=28)
    water_level = result.registers[0] / 100
    print("Water level: ", water_level, " %")
    time.sleep(1)
    clear_output()
