from db.db import DB
from sensor.bme680 import BME680
from sensor.vl53l1x import VL53L1XS
import argparse, config, confuse, datetime, logging, signal, sys, time


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-d", "--dryrun", help="run without writing to the database", action="store_true")
args = parser.parse_args()

if args.verbose:
  logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', level=logging.DEBUG)
else: 
  logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', level=logging.INFO)

config = confuse.LazyConfig('soursensor')

db = DB(config['databases']['influxdb'])

sensors = []
sensors.append(BME680())
sensors.append(VL53L1XS(config['sensors']['VL53L1X']))

def exit_handler(signal, frame):
  logging.info('Shutting down sensors...')
  for sensor in sensors:
    sensor.stop()
    logging.info('Sensor ' + sensor.name + ' stopped')
  sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

while True:
  for sensor in sensors:
    data = sensor.get_data()
    for measurement, value in data.items():
      logging.info('Measurement: ' + str(measurement) + ', ' + str(value))
      if not args.dryrun:
        logging.info('Writing measurement to database...')
        db.write(measurement, value)
        logging.info('Write complete')
  time.sleep(60)
