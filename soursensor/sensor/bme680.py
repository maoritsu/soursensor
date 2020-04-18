from subprocess import PIPE, Popen
import bme680, logging, time

class BME680():

    def __init__(self):
      self.name = 'BME680'
      try:
          self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
      except IOError:
          self.sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

      # These oversampling settings can be tweaked to
      # change the balance between accuracy and noise in
      # the data.
      self.sensor.set_humidity_oversample(bme680.OS_2X)
      self.sensor.set_pressure_oversample(bme680.OS_4X)
      self.sensor.set_temperature_oversample(bme680.OS_8X)
      self.sensor.set_filter(bme680.FILTER_SIZE_3)

      # Disable gas measurements
      self.sensor.set_gas_status(bme680.DISABLE_GAS_MEAS)

    def get_data(self):
      self.sensor.get_sensor_data()

      return {
        "temperature": self.sensor.data.temperature,
        "pressure": self.sensor.data.pressure,
        "humidity": self.sensor.data.humidity,
      }
    
    def stop(self):
      pass
