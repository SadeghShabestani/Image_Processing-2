import cv2

image_a = cv2.imread('pic/board - origin.bmp')
image_b = cv2.imread('pic/board - test.bmp')

image_a = cv2.cvtColor(image_a, cv2.COLOR_RGB2GRAY)
image_b = cv2.cvtColor(image_b, cv2.COLOR_RGB2GRAY)
image_b = cv2.flip(image_b, 1)
image_result = cv2.subtract(image_a, image_b) * 10

cv2.imshow('Image Output', image_result)
cv2.imwrite('README.jpg', image_result)
cv2.waitKey()
