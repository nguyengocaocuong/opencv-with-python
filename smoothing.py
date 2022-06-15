import cv2 as cv 

img =  cv.imread('.\Photos\cats.jpg')

# Averaginh
average = cv.blur(img,(3,3))
cv.imwrite('output/average.jpg', average)

# Gaussia Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imwrite('output/gauss.jpg', gauss)

# Median Blur
median = cv.medianBlur(img,3)
cv.imwrite('output/median.jpg', median)
