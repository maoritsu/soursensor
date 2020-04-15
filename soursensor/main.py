from sensor.bme680 import BME680
import datetime
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError


sensor = BME680()
data = sensor.get_data()
print(data)

USER = 'root'
PASSWORD = 'root'
DBNAME = 'soursensor'

host = 'localhost'
port = 8086

point = {
  "time": datetime.datetime.utcnow(),
  "measurement": "temperature",
  "fields": {
    "value": data['temperature'],
  },
  "tags": {
    "tag": "tag",
  }
}

client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)

client.write_points([point])
