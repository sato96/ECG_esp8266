print('Booting...')
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')

        ssid = 'Ecg-WIFI'
        password = '123456789'

        ap = network.WLAN(network.AP_IF)
        ap.active(True)
        ap.config(essid=ssid, password=password)

        # sta_if.active(True)
        # sta_if.connect('Vodafone-A44562520_plus', 'N77gcXqb3qesMTdR')
        # while not sta_if.isconnected():
        #     pass
        while ap.active() == False:
            pass

        print('Connection successful')
    print(ap.ifconfig())
    #print('network config:', sta_if.ifconfig())
do_connect()
