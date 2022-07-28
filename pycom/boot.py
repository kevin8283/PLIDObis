SSID = "Notebook"
KEY = "123456789"

def connect(ssid, key):
    import network

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, key)
        while not wlan.isconnected():
            pass
    
    print('network config:', wlan.ifconfig())

connect(SSID, KEY)