from db.db import DB
from sensor.bme680 import BME680
import datetime, time

db = DB()

sensors = []
sensors.append(BME680())

while True:
  for sensor in sensors:
    data = sensor.get_data()
    for measurement, value in data.items():
      #db.write(measurement, value)
      print('Measurement inserted into db: ' + str(measurement) + ', ' + str(value))
  time.sleep(5)
