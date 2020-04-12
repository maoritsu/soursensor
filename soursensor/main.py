#!/usr/bin/python3

from sensor.bme680 import BME680

sensor = BME680()
print(sensor.get_data())




