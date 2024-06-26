# coding: utf-8
import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile('shota_Imanaga.jpg'))
print(img.shape)
cv.imshow('test', img)
k=cv.waitKey(0)
