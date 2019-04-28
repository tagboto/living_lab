#from tinydb import TinyDB, Query
import Adafruit_DHT as dht    # Importing Adafruit library for DHT22
from time import sleep,time           # Impoting sleep from time library to add delay
from datetime import datetime

def check_humidity():
#	db = TinyDB('db.json')
#	humi_tbl = db.table('humidity')
#	temp_tbl = db.table('temperature')

	while True:                # Loop will run forever
		humi, temp = dht.read_retry(dht.DHT22, 4)  # Reading humidity and temperature
		my_time = time()*1000
		#humi_tbl.insert({'Time':my_time},{'Humidity':humi})
		#temp_tbl.insert({'Date':date},{'Temp':temp})
		print('Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(temp, humi))
		#print(temp)
		#print(my_time)
		sleep(5)


