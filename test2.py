import cmath as math
from turtle import clear
import cv2
a = math.pi
b = math.e
c = a*b
print('a + b = ',a+b)
print('c = a*b =',c)
img = cv2.imread('test.jpeg')
cv2.imshow('test.jpeg', img)
cv2.waitKey(0)
