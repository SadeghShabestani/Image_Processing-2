import cv2

image = cv2.imread('pic/chess pieces.jpg')

image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

print(image.shape)

chess = []
# chess1 = image[120: 250, 0:75]
# cv2.imwrite('pic/result/chess1.jpg', chess1)
# chess2 = image[120: 250, 75:150]
# cv2.imwrite('pic/result/chess2.jpg', chess2)
# chess3 = image[50: 250, 150:250]
# cv2.imwrite('pic/result/chess3.jpg', chess3)
# chess4 = image[70: 250, 250:340]
# cv2.imwrite('pic/result/chess4.jpg', chess4)
# chess5 = image[100: 250, 340:420]
# cv2.imwrite('pic/result/chess5.jpg', chess5)
# chess6 = image[110: 250, 420:500]
# cv2.imwrite('pic/result/chess6.jpg', chess6)
# chess7 = image[110: 250, 500:590]
# cv2.imwrite('pic/result/chess7.jpg', chess7)

image1 = cv2.hconcat([cv2.imread('pic/result/chess1.jpg'), cv2.imread('pic/result/chess6.jpg')])
image2 = cv2.hconcat([cv2.imread('pic/result/chess3.jpg'), cv2.imread('pic/result/chess2.jpg')])
image3 = cv2.hconcat([image1, image2])
image4 = cv2.hconcat([cv2.imread('pic/result/chess5.jpg'), cv2.imread('pic/result/chess4.jpg')])
image5 = cv2.hconcat([cv2.imread('pic/result/chess7.jpg')])
image6 = cv2.hconcat([image4, image5])
image_result = cv2.hconcat([image3, image6])

cv2.imshow('Image Output', image_result)
cv2.imwrite('README.jpg', image_result)
cv2.waitKey()
