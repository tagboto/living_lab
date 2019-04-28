#Code from PiddlerInTheRoot Sound Sensor(Raspberry Pi) - Youtube Video
#Importing the GPIO library and the time
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 17 #Connected to PIN 17 of the pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# Prints sound detected if there is a change detected in the input
def callback(channel):
	if GPIO.input(channel):
		print("Sound Detected!")

	else:
		print("Sound Detected!")

GPIO.add_event_detect(channel,GPIO.BOTH, bouncetime=300) #let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback) #call back function will work if the input changes

#infinite loop
while True:
	time.sleep(5) #small wait inbetween
