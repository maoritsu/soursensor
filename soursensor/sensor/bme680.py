import bme680
import time


class BME680():

    def __init__(self):
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
      self.sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
      self.sensor.set_gas_heater_temperature(320)
      self.sensor.set_gas_heater_duration(150)
      self.sensor.select_gas_heater_profile(0)

      # Up to 10 heater profiles can be configured, each
      # with their own temperature and duration.
      # sensor.set_gas_heater_profile(200, 150, nb_profile=1)
      # sensor.select_gas_heater_profile(1)

    def get_data(self):
      self.sensor.get_sensor_data()
      return {
        "temperature": self.sensor.data.temperature,
        "pressure": self.sensor.data.pressure,
        "humidity": self.sensor.data.gas_resistance,
      }
