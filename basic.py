import cv2 as cv 

img = cv.imread('Photos/park.jpg')

#Converting to grayscale
cv.imwrite('output/grayscale.jpg',cv.cvtColor(img,cv.COLOR_BGR2GRAY))

# Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imwrite('output/blur.jpg',blur)

#Edge Cascade
canny = cv.Canny(blur,125,175)
cv.imwrite('output/Canny.jpg',canny)

#Dilating the iamge
dilated = cv.dilate(canny,(7,7),iterations=3)

#Eroding
eroded =cv.erode(dilated,(7,7),iterations=3)
cv.imwrite('output/eroded.jpg',eroded)

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imwrite('output/resized.jpg',resized)

#Cropping
cropped = img[50:200,200:400]
cv.imwrite('output/cropped.jpg',cropped)


