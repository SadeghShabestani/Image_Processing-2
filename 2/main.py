import cv2
import numpy as np


def image(num):
    images = []
    for i in range(1, 5):
        img = cv2.imread(f'pic/{num}/{i}.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = cv2.resize(img, (600, 600))
        images.append(img)

        for image in images:
            image_result = image // len(images)

        cv2.imwrite(f'pic/result/res{num}.jpg', image_result)


image(1)
image(2)
image(3)
image(4)

image1 = cv2.vconcat([cv2.imread('pic/result/res1.jpg'), cv2.imread('pic/result/res3.jpg')])
image2 = cv2.vconcat([cv2.imread('pic/result/res2.jpg'), cv2.imread('pic/result/res4.jpg')])

image3 = cv2.hconcat([image1, image2])

cv2.imshow('Image Output', image3)
cv2.imwrite(f'README.jpg', image3 * 2)
cv2.waitKey()
