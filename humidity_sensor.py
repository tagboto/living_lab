#from tinydb import TinyDB, Query
import Adafruit_DHT as dht    # Importing Adafruit library for DHT22
from time import sleep,time           # Impoting sleep from time library to add delay
from datetime import datetime

def check_humidity():

	while True:                # Loop will run forever
		humi, temp = dht.read_retry(dht.DHT22, 4)  # Reading humidity and temperature
		my_time = time()*1000
		print('Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(temp, humi))
		return(temp,humi)
		sleep(2)


#check_humidity()
