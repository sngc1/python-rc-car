import time

import RPi.GPIO as GPIO

SPEED_STOP = 6.6
SPEED_MAX = 10.0 # TBD

PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

servo = GPIO.PWM(PIN, 50)
servo.start(SPEED_STOP)
time.sleep(1)

try:
    while True:
        i = SPEED_STOP
        while i < SPEED_MAX:
            servo.ChangeDutyCycle(i)
            i += 0.1
            time.sleep(1)


        while i > SPEED_STOP:
            servo.ChangeDutyCycle(i)
            i -= 0.1
            time.sleep(1)
finally:
    servo.stop()
    GPIO.cleanup()

print('done')

