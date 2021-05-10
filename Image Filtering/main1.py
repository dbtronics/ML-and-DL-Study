import cv2
import numpy as np

img = cv2.imread('numbers.jpg', 0)
cv2.imshow('before', img)
cv2.waitKey(0)
threshold_num = [55, 90, 150]
for i in threshold_num:
    img2 = img.copy()
    for row in img2:
        for j in range(len(row)):
            if row[j] > i:
                row[j] = 255
            else:
                row[j] = 0
    cv2.imshow('after {} threshold'.format(i), img2)
    cv2.waitKey(0)



