import cv2

image_a = cv2.imread('pic/a.tif')
image_b = cv2.imread('pic/b.tif')

image_a = cv2.cvtColor(image_a, cv2.COLOR_RGB2GRAY)
image_b = cv2.cvtColor(image_b, cv2.COLOR_RGB2GRAY)
image_result = cv2.subtract(image_b, image_a)

rows, columns = image_result.shape
for i in range(rows):
    for j in range(columns):
        image_result[i, j] = 255 - image_result[i, j]

cv2.imshow('Image Output', image_result)
cv2.imwrite('README.jpg', image_result)
cv2.waitKey()
