ECG esp8266. It uses AD8232 module and a led. If you wan to get data you can connect to AP and then open socket connection.

Pin schema:
pmin is a logical value that controll electrode adhesion,it is in Pin 5
pmax is a logical value that controll electrode adhesion,it is in Pin 4
The esp gets signal from ADC, reading it.
To know while system is recording there is a white led, in Pin 10
