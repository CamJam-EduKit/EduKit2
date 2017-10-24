# CamJam EduKit 2 - Sensors (GPIO Zero)
# Worksheet 6 - Alarm

# Import Python header files
from gpiozero import MotionSensor, LED, Buzzer
import time

# Set a variable to hold the GPIO Pin identity
pir = MotionSensor(17)
red = LED(18)
blue = LED(24)
buzzer = Buzzer(22)

print("Waiting for PIR to settle")
pir.wait_for_no_motion()

print("PIR Module Test (CTRL-C to exit)")

# Variables to hold the current and last states
currentstate = False
previousstate = False

try:
    # Loop until users quits with CTRL-C
    while True:
        # Read PIR state
        currentstate = pir.motion_detected

        # If the PIR is triggered
        if currentstate == True and previousstate == False:
            print("    Motion detected!")
            # Flash lights and sound buzzer three times
            for x in range(0, 3):
                buzzer.on()
                red.on()
                time.sleep(0.2)
                red.off()
                blue.on()
                time.sleep(0.2)
                blue.off()
                buzzer.off()
                time.sleep(0.2)

                # Record previous state
                previousstate = True
        # If the PIR has returned to ready state
        elif currentstate == False and previousstate == True:
            print("    No Motion")
            previousstate = False

        # Wait for 10 milliseconds
        time.sleep(0.01)

except KeyboardInterrupt:
    print("    Quit")
