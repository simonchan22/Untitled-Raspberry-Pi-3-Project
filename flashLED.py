import sys
import wiringpi2 as wpi
from time import sleep
pirnt "Starting the Python wiringPi example"
wpi.wiringPiSetupGpio()
wpi.pinMode(17,1)
wpi.pinMode(27,0)
ledout = wpi.digitalRead(17)
button = wpi.digitalRead(27)
while buttonout == 0:
	wpi.digitalWrite(17,1)
	sleep(0.5)
	wpi.digitalWrite(17,1)
	sleep(0.5)
print ("Button pressed to end the example")
	