#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)



while(1):

    # Frame alinma islemi
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    # define range of blue color in HSV
    minDeger = np.array([10,50,50])
    maxDeger = np.array([170,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, minDeger, maxDeger)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # Goruntuleri pencerelere basma islemleri
    cv2.namedWindow('orjinal goruntu', cv2.WINDOW_NORMAL)
    cv2.imshow('orjinal goruntu',frame, )

    cv2.namedWindow('maskelenmis', cv2.WINDOW_NORMAL)
    cv2.imshow('maskelenmis',mask)

    cv2.namedWindow('sonuc', cv2.WINDOW_NORMAL)
    cv2.imshow('sonuc',res)


    # ESC'ye basma işleminde penceleri kapatması işlemi
    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.realese()