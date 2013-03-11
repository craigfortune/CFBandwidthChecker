import urllib2
import time

# For Raspberry Pi GPIO access
import RPi.GPIO as GPIO

# Available: https://github.com/teeks99/speed_check
# I've included them alongside this file for a 'quick start'
import SpeedCheck as SC

# Does the actual speed check and returns avg speed
def doTest(time, block, msg_freq):
    url = 'http://speedtest.wdc01.softlayer.com/downloads/test500.zip'

    f = urllib2.urlopen(url)
    average, bytes, elapsed, block = SC.speed_check_info(f, time, block, msg_freq)
    f.close()

    return average

# Utility function to get the result in a neater MBit/sec format
# e.g. 3.44
def speedInMBit(speed):
    return round(speed / 1024 / 1024 * 8, 2)

# Default pins on the RPi GPIO to use
redLED = 11
yellowLED = 12
greenLED = 15

# Default bands of connection Speed
fastSpeed = 6
mediumSpeed = 4
slowSpeed = 2

# Setup GPIO
def setup():
    GPIO.setup(redLED, GPIO.OUT)
    GPIO.setup(yellowLED, GPIO.OUT)
    GPIO.setup(greenLED, GPIO.OUT)

    blankPins()

# Set all the LEDs to off
def blankPins():
    GPIO.output(redLED, False)
    GPIO.output(yellowLED, False)
    GPIO.output(greenLED, False)

# Starting point
if __name__ == '__main__':
    setup()
    while(True):
        # Default settings for the bandwidth check
        # Might want to tweak these
        speed = speedInMBit(doTest(10, 1024, 0))

        # Blank the LEDs and have a brief wait
        # This is useful so you know the system is still
        # updating and hasn't just stopped if your connection
        # happens to be nice and stable
        blankPins()
        time.sleep(0.4)

        # Light the LEDs up accordingly
        if(speed > fastSpeed):
            GPIO.output(greenLED, True)
        if(speed > mediumSpeed):
            GPIO.output(yellowLED, True)
        if(speed > slowSpeed):
            GPIO.output(redLED, True)

        # Delay for 40 seconds - otherwise we'll simply be hammering our
        # connection constantly
        time.sleep(40)
