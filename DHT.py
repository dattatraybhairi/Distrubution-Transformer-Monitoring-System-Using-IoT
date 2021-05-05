# import standard python modules.
import time
 
# import adafruit dht library.
import Adafruit_DHT

# Delay in-between sensor readings, in seconds.
DHT_READ_TIMEOUT = 5
 
# Pin connected to DHT22 data pin
DHT_DATA_PIN = 5
 
 # Set up DHT22 Sensor.
dht11_sensor = Adafruit_DHT.DHT11

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht11_sensor, DHT_DATA_PIN)
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
    time.sleep(DHT_READ_TIMEOUT)