import socket
import json
import beebotte
import config_bbt #secret keys
import time
import pprint

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 33033))

bbt = beebotte.BBT(config_bbt.API_KEY, config_bbt.SECRET_KEY)

def to_bbt(channel, res_name, json_datas):
    data_list = []

    for e in json_datas:
        data_list.append({"resource": res_name,
                            "data" : int(e),
                            "ts": int(time.time() * 1000)})

    pprint.pprint(data_list)

    bbt.writeBulk(channel, data_list)


while True:
    data, addr = s.recvfrom(1500)

    j = json.loads(data)
    to_bbt("capteurs", "temperature", j)