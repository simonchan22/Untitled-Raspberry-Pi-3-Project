import sys
import wiringpi as wpi
from time import sleep
print "Starting the Python wiringPi example"
wpi.wiringPiSetupGpio()
wpi.pinMode(17,1)
wpi.pinMode(27,0)
while wpi.digitalRead(27) == 0:
	wpi.digitalWrite(17,1)
	sleep(0.5)
	wpi.digitalWrite(17,0)
	sleep(0.5)
print ("Button pressed to end the example")
wpi.digitalWrite(17,0)
#JUst to check if the branch get updated
	
