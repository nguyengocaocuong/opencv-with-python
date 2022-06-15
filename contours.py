import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/cats.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


blank = np.zeros(img.shape, dtype='uint8')
# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imwrite('test1.jpg',blur)

# canny = cv.Canny(blur,125,175)
# cv.imwrite('test.jpg',canny)

ret, thesh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(thesh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)}')

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imwrite('test2.jpg',blank)

# cv.imwrite('test.jpg',canny)
