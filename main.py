import machine
import utime
import socket


print('Connession adc...')
adc = machine.ADC(0)


html = """<!DOCTYPE html>
<html>
    <head> <title>Elettrocardiografo</title> </head>
    <body> <h1>ECG</h1>
        <div> %s </div>
    </body>
</html>
"""

pmin = machine.Pin(5, machine.Pin.IN)
pplus = machine.Pin(4, machine.Pin.IN)
led = machine.Pin(10, machine.Pin.OUT)

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

fl_record = 0
while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    request = cl.recv(1024)
    request = str(request)
    print(request)
    msgSplit = request.split(' ')
    print(msgSplit[0])
    if msgSplit[0] == "b'GET" and msgSplit[1] == '/ecg':
        try:
            while True:
                # ricordarsi per capire se gli elettrodi sono ok
                led.value(1)
                if pmin.value() == 1 or pplus.value() == 1:
                    #campione = str(adc.read()) + '\n'
                    #cl.send(campione)
                    print('error')
                else:
                    campione = str(adc.read()) + '\n'
                    cl.send(campione)
                utime.sleep(0.01)
        except:
            led.value(0)
            cl.close()
    elif msgSplit[0] == "b'GET" and msgSplit[1] == '/':
        response = html
        response = response.replace('%s', '<a href="/ecg">Inizia la registrazione</a>')
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
    else:
        cl.send('HTTP/1.0 500 KO\r\nContent-type: text/html\r\n\r\n')
        cl.close()
    #115200

