# CamJam EduKit 2 - Sensors
# Worksheet 5 - Movement

# Import Python header files
import time
from gpiozero import MotionSensor

# Set a variable to hold the GPIO Pin identity
pir = MotionSensor(17)

print("Waiting for PIR to settle")
pir.wait_for_no_motion()

print("PIR Module Test (CTRL-C to exit)")


try:
    # Variables to hold the current and last states
    current_state = False
    previous_state = False

    # Loop until users quits with CTRL-C
    while True:
        # Read PIR state
        current_state = pir.motion_detected

        # If the PIR is triggered by movement.
        if current_state is True and previous_state is False:
            print("    Motion detected!")
            # Record previous state
            previous_state = True
        # If the PIR has returned to ready state
        elif current_state is False and previous_state is True:
            print("    No Motion")
            previous_state = False

        # Wait for 10 milliseconds
        time.sleep(0.01)

except KeyboardInterrupt:
    print("    Quit")
