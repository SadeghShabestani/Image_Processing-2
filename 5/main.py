import cv2
import numpy as np

images = []
for image in range(1, 15):
    img = cv2.imread(f'pic/h{image}.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img, (400, 300))
    images.append(img)
rows, columns = images[1].shape
image_result = np.zeros((rows, columns), dtype='uint8')

for image in images:
    image_result += image // len(images)

cv2.imshow('Image Output', image_result)
cv2.imwrite('README.jpg', image_result)
cv2.waitKey()
