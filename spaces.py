import cv2 as cv 

img = cv.imread('Photos/cats.jpg')

# BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imwrite('output/gray.jpg',gray)

#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imwrite('output/hsv.jpg',hsv)

#BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imwrite('output/lab.jpg', lab)