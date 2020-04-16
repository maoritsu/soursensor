from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket='soursensor'
url='https://eu-central-1-1.aws.cloud2.influxdata.com'
token='Ok2vPSGFZ8wYQ5Qn9dRzMUl8crkS8D11nLJRf67Qioxo0qbABpMQ8Vz6cmieI3-RY7P1-5qOHjgwJXSIxIOyMg=='
org='soursensor'

class DB():

  def __init__(self):
    self.client = InfluxDBClient(url=url, token=token, org=org)
    self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
  
  def write(self, measurement, value):
    record = Point(measurement).field('value', value)
    self.write_api.write(bucket=bucket, record=record)

