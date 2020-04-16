from subprocess import PIPE, Popen
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

      # Disable gas measurements
      self.sensor.set_gas_status(bme680.DISABLE_GAS_MEAS)
      
      # CPU temperature compensation
      self.smoothing_factor = 1.0  # Smaller numbers adjust temp down, vice versa
      self.smooth_size = 10  # Dampens jitter due to rapid CPU temp changes
      self.cpu_temps = [] # Store rolling series of CPU temps

    def get_data(self):

      self.sensor.get_sensor_data()

      cpu_temp = self._get_cpu_temperature()
      self.cpu_temps.append(cpu_temp)

      if len(self.cpu_temps) > self.smooth_size:
        self.cpu_temps = self.cpu_temps[1:]

      smoothed_cpu_temp = sum(self.cpu_temps) / float(len(self.cpu_temps))
      raw_temp = self.sensor.data.temperature
      comp_temp = raw_temp - ((smoothed_cpu_temp - raw_temp) / self.smoothing_factor)

      return {
        "raw_temperature": raw_temp,
        "compensated_temperature": comp_temp,
        "pressure": self.sensor.data.pressure,
        "humidity": self.sensor.data.gas_resistance,
      }

    def _get_cpu_temperature(self):
      process = Popen(['cat', '/sys/class/thermal/thermal_zone0/temp'], stdout=PIPE)
      output, _error = process.communicate()
      return float(output) / 1000

