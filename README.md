# Soursensor

## Initial setup

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

Start soursensor by running `python soursensor/main.py`.