import time

import RPi.GPIO as GPIO

# MG996R: 50Hz (20ms), 
#   771(0.771ms) - 2193(2.19ms) 
#   3.8% - 10.95
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

