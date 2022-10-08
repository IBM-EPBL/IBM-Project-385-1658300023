#importing necessary libraries
import RPI.GPIO as gpio
from time import sleep

RED_PIN = 25
YELLOW_PIN =8 
GREEN_PIN =7

gpio.setwarnings(FALSE)
gpio.setmode(gpio.BOARD)    

def set_red_light():
        gpio.output(RED_PIN, gpio.HIGH)
        gpio.output(YELLOW_PIN, gpio.LOW)
        gpio.output(GREEN_PIN, gpio.LOW)

def set_yellow_light():
        gpio.output(RED_PIN, gpio.LOW)
        gpio.output(YELLOW_PIN, gpio.HIGH)
        gpio.output(GREEN_PIN, gpio.LOW)

def set_green_light():
        gpio.output(RED_PIN, gpio.LOW)
        gpio.output(YELLOW_PIN, gpio.LOW)
        gpio.output(GREEN_PIN, gpio.HIGH)

def trafficSignl():
    while True:
        set_red_light() # block traffic for 10 seconds
        sleep(10)

        set_yellow_light()  # yellow for 2 seconds
        sleep(2)
        
        set_green_light()
        sleep(5)    # allow traffic for 5 seconds
