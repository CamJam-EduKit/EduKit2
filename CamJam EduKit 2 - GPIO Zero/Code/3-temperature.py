# CamJam EduKit 2 - Sensors
# Worksheet 3 - Temperature

# Import Libraries
import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

# Print out the temperature until the program is stopped.
while True:
    print(sensor.get_temperature(W1ThermSensor.DEGREES_C), "Celcius")
    time.sleep(1)
