# CamJam EduKit 2 - Sensors
# Worksheet 3 - Temperature

# Import Libraries
import time
from w1thermsensor import W1ThermSensor, Unit

sensor = W1ThermSensor()

# Print out the temperature until the program is stopped.
while True:
    temp_c = sensor.get_temperature(Unit.DEGREES_C)
    temp_f = sensor.get_temperature(Unit.DEGREES_F)

    print(temp_c, " Celsius")
    print(temp_f, " Fahrenheit")

    time.sleep(1)
