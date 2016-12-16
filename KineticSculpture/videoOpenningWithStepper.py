# -*- coding: utf-8 -*-
#import RPi.GPIO as GPIO
#import os
#import sys
import time
import random

#from subprocess import Popen

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

movie1 = ("/home/pi/Desktop/Proje/video1.mp4")
movie2 = ("/home/pi/Desktop/Proje/video1.mp4")
movie3 = ("/home/pi/Desktop/Proje/video1.mp4")
movie4 = ("/home/pi/Desktop/Proje/video1.mp4")
movie5 = ("/home/pi/Desktop/Proje/video1.mp4")
movie6 = ("/home/pi/Desktop/Proje/video1.mp4")
movie7 = ("/home/pi/Desktop/Proje/video1.mp4")

player = False

flag = True


def main():  # Ana fonksiyon ##################################################
    while True:
        motorRandomDonus(flag)

        flagIslem()


        # end while


# end def main

def motorRandomDonus(flag):  ##################################################

    if flag == True:
        print "Motor random donuyor.."
    # end if

    else:  # flag == False
        print "Motor durdu"
        # end else


# end def motorRandomDonus

def sensorOkuma(self):  # Sensor okuma interrupti ##############################
    print "Sensor goruldu"

    global flag

    if flag == False:
        flag = True
    # end if

    else:
        flag = False
        # end else


# end def sensorOkuma

#GPIO.add_event_detect(21, GPIO.FALLING, callback=sensorOkuma, bouncetime=100)


def flagIslem():  # flag durum fonksiyonu ######################################
    global flag
    if flag != True:


        print "Selam Millet"
        #os.system('killall omxplayer.bin')
        #omxc = Popen(['omxplayer', '-b', movie1])
        #player = True
        flag = True

        time.sleep(3)
        # end if

        # else:
        # print "malesef"
        # end else


# end def flagIslem


if __name__ == "__main__":
    main()
