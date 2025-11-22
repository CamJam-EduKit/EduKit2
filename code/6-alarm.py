# CamJam EduKit 2 - Sensors
# Worksheet 6 - Alarm

# Import Python header files
import time
from gpiozero import MotionSensor, LED, Buzzer

# Set a variable to hold the GPIO Pin identity
pir = MotionSensor(17)
red = LED(18)
blue = LED(24)
buzzer = Buzzer(22)

print("Waiting for PIR to settle")
pir.wait_for_no_motion()

print("PIR Module Test (CTRL-C to exit)")


def sound_alarm():
    # Flash the LEDs and sound buzzer three times
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


try:
    # Variables to hold the current and last states
    current_state = False
    previous_state = False

    # Loop until users quits with CTRL-C
    while True:
        # Read PIR state
        current_state = pir.motion_detected

        # If the PIR is triggered
        if current_state is True and previous_state is False:
            print("    Motion detected!")
            sound_alarm()

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
