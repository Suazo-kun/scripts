"""
This script checks if a bluetooth device, whose name has been previously
provided, is connected and if this condition is met it launches the RetroArch
program.
"""

import subprocess
from time import sleep

# Devices name.
DEVICE = ''
# RetroArch path.
RETROARCH_PATH = ''

print(f'INFO: Wait for device: {DEVICE}.')
while True:
    sleep(0.1)

    try:
        result = subprocess.run(
            'bluetoothctl devices Connected', shell=True,
            capture_output=True, text=True
        ).stdout
    except subprocess.CalledProcessError:
        print(
            'ERROR: The attempt to check the devices connected to the '
            'bluetooth network failed. Wait five seconds for the next attempt.'
        )
        sleep(4.9)
        continue

    if DEVICE in result:
        try:
            print('INFO: Starting RetroArch.')
            subprocess.run(RETROARCH_PATH, shell=True)
            print('INFO: RetroArch has been closed.')
        except subprocess.CalledProcessError:
            print('ERROR: Failed attempt to launch RetroArch.')
