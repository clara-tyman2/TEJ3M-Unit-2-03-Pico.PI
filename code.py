# Created by Clara T

# Created on Feb 2025

# Blink with Breadboard and LED with resistor

# Turns LED on for one second, the off for one second, each time increases each time by 1 more second


import time
import board
import digitalio

blink_time = 1
led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

while True:
    print(blink_time)
    led.value = True # LED On
    time.sleep(blink_time) # Wait for 1000 millisecond(s)
    led.value = False # LED Off
    time.sleep(blink_time) # Wait for 1000 millisecond(s)

    blink_time = blink_time + 1 # Add 1 second to the variable blink_time