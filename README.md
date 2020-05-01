# Soursensor
Soursensor is a tool for monitoring the activity of sourdough starter. Soursensor integrates with [VL53L1X](https://www.st.com/en/imaging-and-photonics-solutions/vl53l1x.html) and [BME680](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors-bme680) sensors for measuring the rise of the starter and ambient conditions (temperature, relative humidity and pressure) respectively.

## Dependencies
You'll need a raspberry pi, a BME680 gas sensor for measuring temperature, relative humidity and pressure; and a VL53L1X ranging time-of-flight sensor for measuring the rise of the starter. The sensors are available as breakouts which interface with the pi i2c bus [here](https://shop.pimoroni.com/products/bme680-breakout) and [here](https://shop.pimoroni.com/products/vl53l1x-breakout).

## Setting up a new raspbery pi

Change the default password for user `pi`. Create a new user and add them to the `sudo` group:
```
sudo adduser bob
sudo adduser bob sudo
```

Enable i2c, add the new user to the `i2c` group and restart:

```
sudo raspi-config
sudo usermod -a -G i2c bob
sudo shutdown -r now
```

## Installing the necessary libraries

Install necessary packages and libraries for git and python:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git python3 python3-venv python3-pip
```

Clone the soursensor repo:

```
mkdir /home/user/code
cd /home/user/code
git clone https://github.com/maoritsu/soursensor.git
```

Install python `virtualenv` and create a virtual environment:

```
pip install virtualenv
python3 -m venv .venv
source .venv/bin/activate
```

Install the necessary python packages for soursensor:
```
pip install bme680 vl53l1x wheel influxdb-client config confuse smbus
```

Add the soursensor configuration file `config.yaml` in `/home/user/.config/soursensor`.

## Running

Start soursensor after activating the virtual environment:

```
source .venv/bin/activate
python soursensor/main.py
 ```
