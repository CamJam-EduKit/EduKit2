# CamJam EduKit 2 - Sensors
# Worksheet 6 - Alarm

# Import Python header files
import RPi.GPIO as GPIO
import time

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinpir = 17
pinredled = 18
pinblueled = 24
pinbuzzer = 22

print("PIR Module Test (CTRL-C to exit)")

# Set pins as input/output
GPIO.setup(pinpir, GPIO.IN)
GPIO.setup(pinredled, GPIO.OUT)
GPIO.setup(pinblueled, GPIO.OUT)
GPIO.setup(pinbuzzer, GPIO.OUT)

# Variables to hold the current and last states
currentstate = 0
previousstate = 0

try:
    print("Waiting for PIR to settle ...")
    # Loop until PIR output is 0
    while GPIO.input(pinpir) == 1:
        currentstate = 0

    print("    Ready")
    # Loop until users quits with CTRL-C
    while True:
        # Read PIR state
        currentstate = GPIO.input(pinpir)

        if currentstate == 1 and previousstate == 0:
            # PIR is triggered
            print("    Motion detected!")
            # Flash lights and sound buzzer three times
            for x in range(0, 3):
                GPIO.output(pinbuzzer, GPIO.HIGH)
                GPIO.output(pinredled, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(pinredled, GPIO.LOW)
                GPIO.output(pinblueled, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(pinblueled, GPIO.LOW)
                GPIO.output(pinbuzzer, GPIO.LOW)
                time.sleep(0.2)

            # Record previous state
            previousstate = 1

        elif currentstate == 0 and previousstate == 1:
            # PIR has returned to ready state
            print("    Ready")
            previousstate = 0

        # Wait for 10 milliseconds
        time.sleep(0.01)

except KeyboardInterrupt:
    print("    Quit")
    # Reset GPIO settings
    GPIO.cleanup()
