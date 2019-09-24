import time

import RPi.GPIO as GPIO

# MG996R
#   PWM period: 50Hz (20ms), 
#   Available pulse width: 0.771ms - 2.193ms (3.8%-10.95%)

# For Tamiya Hotshot with MG996R TBD
NEWTRAL = 6.5
L_MAX = 4.7
R_MAX = 9

PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

servo = GPIO.PWM(PIN, 50)
servo.start(NEWTRAL)
time.sleep(1)

try:
    while True:
        servo.ChangeDutyCycle(R_MAX)
        time.sleep(1)

        servo.ChangeDutyCycle(L_MAX)
        time.sleep(1)
finally:
    servo.stop()
    GPIO.cleanup()

print('done')

