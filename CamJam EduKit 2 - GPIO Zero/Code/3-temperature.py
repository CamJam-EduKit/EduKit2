# CamJam EduKit 2 - Sensors
# Worksheet 3 - Temperature

# Import Libraries
import time
from w1thermsensor import W1ThermSensor, Unit

sensor = W1ThermSensor()

# Print out the temperature until the program is stopped.
while True:
  temp_C = sensor.get_temperature(Unit.DEGREES_C)
  temp_F = sensor.get_temperature(Unit.DEGREES_F)

  print(temp_C, " Celsius")
  print(temp_F, " Fahrenheit")

  time.sleep(1)
