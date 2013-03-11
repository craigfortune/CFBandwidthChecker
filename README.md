CFBandwidthChecker
==================

Some simple python code that gives you a physical output for your current bandwidth conditions. Running the script will update the GPIO pin settings on pins defined within the script. The pins could be hooked up to 3 LEDs to show 3 different (4, including off) bandwidth states.

The default settings are 2, 4 and 6mbit/sec on pins 11, 12 and 15.

The script waits for 40 seconds before running again. Tweak this value so you aren't hammering your connection too frequently.

The downloading element of the script is from here. All rights to the original author (Tom Kent/teeks99) who kindly made it available for use: https://github.com/teeks99/speed_check

This script will need to be run with sudo due to GPIO usage.
