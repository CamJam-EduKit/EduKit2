# CamJam EduKit 2 - Sensors
# Worksheet 2 - LEDs and Buzzer

# Import Python libraries
import time
from gpiozero import LED, Buzzer

# Set up the LEDs and Buzzer
red = LED(18)
blue = LED(24)
buzzer = Buzzer(22)

print("Lights and sound on")
red.on()
blue.on()
buzzer.on()

# Pause for one second
time.sleep(1)

print("Lights and sound off")
red.off()
blue.off()
buzzer.off()
