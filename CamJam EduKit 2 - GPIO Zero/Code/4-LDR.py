# CamJam EduKit 2 - Sensors (GPIO Zero)
# Worksheet 4 - Light

# Import Libraries
from gpiozero import LightSensor
import time

# A variable with the LDR reading pin number
ldr = LightSensor(27)

while True:
    print(ldr.value)
    time.sleep(1)  # Wait for a second
