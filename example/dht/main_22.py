#LED Blinking on ESP8266 using Micropython:
# https://circuitdigest.com/microcontroller-projects/how-to-progarm-esp8266-for-dht22-using-micropython
from machine import Pin
from time import sleep

LED = Pin(2, Pin.OUT)

while True:
  LED.value(not LED.value())
  sleep(0.5)

#Interfacing DHT22 with ESP2866 using MicroPython:
from machine import Pin
from time import sleep
import dht

dht22 = dht.DHT22(Pin(14))

while True:
  try:
    sleep(2)
    dht22.measure()
    temp = dht22.temperature()
    hum = dht22.humidity()
    print('Temperature: %3.2f C' %temp)
    print('Humidity: %3.2f %%' %hum)
  except OSError as e:
    print('Failed to read data from the DHT22 sensor.')