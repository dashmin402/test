import cmath as math
import cv2
a = math.pi
b = math.e
c = a*b
print('a =',a)
print('b =',b)
print('c =',c)
img = cv2.imread('test.jpeg')
cv2.imshow('test.jpeg', img)
cv2.waitKey(0)
