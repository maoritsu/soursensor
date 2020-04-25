import logging, VL53L1X, time

class VL53L1XS():

  def __init__(self, config):
    self.name = 'VL53L1X'
    self.i2c_bus = config['i2c_bus'].get(int)
    self.i2c_address = config['i2c_address'].get()
    self.sensor = VL53L1X.VL53L1X(i2c_bus=self.i2c_bus, i2c_address=self.i2c_address)
    self.sensor.open()

    # Set distance mode:
    # 1 = Short Range
    # 2 = Medium Range
    # 3 = Long Range
    self.distance_mode = config['distance_mode'].get(int)
    self.sensor.set_distance_mode(self.distance_mode)
    self.oversample_factor = config['oversample_factor'].get(int)
    self.distance_scaling_factor = config['distance_scaling_factor'].get(float)

  def get_data(self):
    self.sensor.start_ranging(0)

    distance = 0.
    for i in range(self.oversample_factor):
      subsample = self.sensor.get_distance()
      logging.debug('Distance sub-sample: ' + str(subsample))
      distance += subsample
      time.sleep(0.1)
    distance /= self.oversample_factor

    self.sensor.stop_ranging()

    return {
      "distance_objective": round(distance, 2),
      "distance_relative": round(1 - distance / self.distance_scaling_factor, 2)
    }

  def stop(self):
    self.sensor.stop_ranging()
