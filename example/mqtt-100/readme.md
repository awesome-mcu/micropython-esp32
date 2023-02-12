
# Flashing ESP32 MicroPython firmware

```
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash 0x0000 YOUR_FIRMWARE.bin
```


# Installing Required MicroPython PIP Packages

Install the following uPip packages. You need to estabish a network connection on the ESP32 board then upip.install the umqtt packages.

```
import upip

upip.install('micropython-umqtt.simple')
upip.install('micropython-umqtt.robust')
```


## MicroPython and Publish over MQTT

```
pip install esptool rshell adafruit-ampy

ampy --port /dev/ttyUSB0 put boot.py
ampy --port /dev/ttyUSB0 put main.py

screen /dev/cu.wchusbserial1420 115200
rshell --buffer-size=30 -p /dev/cu.wchusbserial1420 ls
esptool.py --chip esp32s2 -p /dev/cu.wchusbserial1420 flash_id
```

## REF

https://github.com/gloveboxes/ESP32-MicroPython-BME280-MQTT-Sample/blob/master/Micropython.md
