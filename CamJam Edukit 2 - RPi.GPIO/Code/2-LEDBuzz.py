# CamJam Edukit 2 - Sensors
# Worksheet 2 - LEDs and Buzzer

# Import Python libraries
import RPi.GPIO as GPIO
import time

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the three GPIO pins for Output
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

print("Lights and sound on")
GPIO.output(18, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)

# Pause for one second
time.sleep(1)

print("Lights and sound off")
GPIO.output(18, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

GPIO.cleanup()
