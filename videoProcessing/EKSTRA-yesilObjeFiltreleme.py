#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)



while(1):


    _, frame = cap.read()


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    minDeger = np.array([50,50,50])
    maxDeger = np.array([70,255,255])


    mask = cv2.inRange(hsv, minDeger, maxDeger)


    res = cv2.bitwise_and(frame,frame, mask= mask)


    cv2.namedWindow('orjinal goruntu', cv2.WINDOW_NORMAL)
    cv2.imshow('orjinal goruntu',frame, )

    cv2.namedWindow('maskelenmis', cv2.WINDOW_NORMAL)
    cv2.imshow('maskelenmis',mask)

    cv2.namedWindow('sonuc', cv2.WINDOW_NORMAL)
    cv2.imshow('sonuc',res)



    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.realese()