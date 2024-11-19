# About

A smart sunrise alarm clock project using a Raspberry Pi Zero 2 W, designed to simulate a sunrise with a Zigbee LED strip, play alarm sounds, and integrate with Home Assistant for seamless control.

## Features

- Sunrise Simulation: Gradually brightens a Zigbee-compatible LED strip 
- Alarm Sounds: Plays customizable field recordings through an AUX connected speaker
- Home Assistant Integration: Set alarms and control lights using the Home Assistant app
- AirPlay/Bluetooth Speaker: Use Pi as a speaker for streaming music from iOS devices
- OLED Display: Shows the current time or alarm time when buttons are pressed

## Components

- Raspberry Pi Zero 2 W
- Zigbee LED Strip
- CC2531 USB Dongle (for Zigbee communication)
- PAM Mono Amplifier and Speaker
- 0.91 inch I2C OLED Display
- Physical buttons for user interaction

## folder structure
/src/: Contains all Python scripts and modules.
/config/: Stores configuration files for settings and preferences.
/audio/: Contains audio files used for the alarm or other sound effects.
/logs/: Keeps log files to help debug any issues.

main.py: The main entry point of project that will orchestrate the other components (e.g., setting alarms, turning on lights, playing sounds, etc.).
audio.py: Handles playing audio files and managing audio-related functionality.
display.py: Manages the OLED display, showing the time, alarm status, or other messages.
buttons.py: Handles input from the physical buttons connected to GPIO pins.
gpio_setup.py: Sets up and initializes all GPIO pins for the project.

## first steps
```bash
# You’ll need some essential tools for development and interacting with the hardware
sudo apt install -y python3 python3-pip git i2c-tools
sudo apt-get install -y libjpeg-dev zlib1g-dev
# create env and install dependencies 
python3 -m venv ~/pizzo
source ~/pizzo/bin/activate
pip install Adafruit-Blinka
pip install adafruit-circuitpython-ssd1306
pip install adafruit-circuitpython-display-text
deactivate
```

## Enable I2C on raspi for display
```bash
sudo raspi-config
```
Navigate to Interface Options.
Select I2C and enable it.
Exit raspi-config and reboot.

To run at boot time
```bash
nano /etc/rc.local
```
Add `python3 /root/OLED.py ` to script. 

### Airplay
```bash
# install dependencies
sudo apt install -y shairport-sync

# Configure Shairport Sync
sudo nano /etc/shairport-sync.conf
```

Key settings to check
- Output Device: Ensure the output device is set correctly, especially if you are using a specific audio interface or the onboard PWM audio.
- Volume Control: You may want to adjust the volume control settings to work with your amplifier and speaker.

```bash
# Enable and Start Shairport Sync:
sudo systemctl enable shairport-sync
sudo systemctl start shairport-sync
```

Enable I2C and Other Interfaces: Run sudo raspi-config and do the following:

- Go to Interface Options and enable I2C for the OLED display.
- Enable SPI if you plan to use any SPI-based components later.
- Enable Audio settings if needed.
- reboot