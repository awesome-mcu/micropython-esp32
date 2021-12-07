# -*- coding: utf-8 -*-
"""
example:
https://github.com/GregWoods/wifigui-esp32-upy/blob/cd66f06e93/src/main.py
"""

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)


while True:
    led.value(not led.value())
    sleep(0.5)
