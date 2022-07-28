# boot.py -- run on boot-up

SSID = "Notebook"
KEY = "123456789"

def connect(ssid, key):
    import network
    ap = network.WLAN(network.AP_IF)
    wlan = network.WLAN(network.STA_IF)

    ap.active(False)
    wlan.active(True)

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, key)

        while not wlan.isconnected():
            pass

    print("Connection state: ${}".format(wlan.isconnected()))  
    print('network config:', wlan.ifconfig())

connect(SSID, KEY)