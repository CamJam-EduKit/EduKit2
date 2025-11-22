# CamJam EduKit 2 - Sensors
# Worksheet 4 - Light

# Import Libraries
import time
from RPi import GPIO

# Set up the GPIO Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# The Light Sensor pin number
PIN_LIGHT = 27


def read_ldr():
    ldrcount = 0  # Sets the count to 0
    GPIO.setup(PIN_LIGHT, GPIO.OUT)
    GPIO.output(PIN_LIGHT, GPIO.LOW)
    time.sleep(0.1)  # Drains all charge from the capacitor

    GPIO.setup(PIN_LIGHT, GPIO.IN)  # Sets the pin to be input

    # While the input pin reads 'off' or Low, count
    while GPIO.input(PIN_LIGHT) == GPIO.LOW:
        ldrcount += 1  # Add one to the counter

    return ldrcount


while True:
    print(read_ldr())
    time.sleep(1)  # Wait for a second
