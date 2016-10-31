# Raspberry-PI3-Xbee-Zigbee-
Talking between Raspberry PI3 devices via Xbee (Zigbee RF) modules

I have connected the Xbee device (with USB explorer) in first RPi3 board.
And connected other Xbee module to second Xbee.


At first RPi3 board:
sudo python receive_EXbee_Titus.py /dev/ttyUSB0


At second RPi3 board:
sudo python send_EXbee_Titus.py 0013A20040E793E8 "Hello Rpi3... :\)" /dev/ttyUSB0
