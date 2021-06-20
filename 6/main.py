import cv2
import numpy as np

image_a = cv2.imread('pic/Mona_Lisa.jpg')
image_b = cv2.imread('pic/b.jpg')

image_a = cv2.cvtColor(image_a, cv2.COLOR_RGB2GRAY)
image_b = cv2.cvtColor(image_b, cv2.COLOR_RGB2GRAY)

image_a = cv2.resize(image_a, (256, 256))

image_result = image_a / image_b

cv2.imshow('Image Output', image_result)
cv2.imwrite('README.jpg', image_result * 255)
cv2.waitKey()
