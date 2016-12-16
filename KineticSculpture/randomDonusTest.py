#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22, False)


def motorDondur():
    count = 0

    sayac = random.randrange(5, 50, 1)
    zaman = random.randrange(1, 100, 50)
    sonzaman = zaman / 10000.000

    while (count < sayac):
        print "count > " + str(count) + " " + str(zaman) + " " + str(sonzaman)
        GPIO.output(17, False)

        time.sleep(sonzaman)
        GPIO.output(17, True)
        time.sleep(sonzaman)
        count = count + 1

        # end while


# end def motorDondur()

def main():
    while True:
        print "motor donuyor"
        motorDondur()


if __name__ == "__main__":
    main()

