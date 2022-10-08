#importing necessary libraries
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial = GPIO.LOW)
while True:
     GPIO.output(7, GPIO.HIGH)
     sleep(3)
     GPIO.output(7, GPIO.LOW)
     sleep(3)
