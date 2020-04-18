from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

class DB():

  def __init__(self, config):
    self.bucket = config['bucket'].get()
    self.org = config['org'].get()
    self.token = config['token'].get()
    self.url = config['url'].get()

    self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
    self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
  
  def write(self, measurement, value):
    record = Point(measurement).field('value', value)
    self.write_api.write(bucket=self.bucket, record=record)

