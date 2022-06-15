import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/park.jpg')

#split chanel color
b, g, r = cv.split(img)
cv.imwrite('output/blue_chanel.jpg',img[:,:,:1])
cv.imwrite('output/green_chanel.jpg',img[:,:,1:2])
cv.imwrite('output/red_chanel.jpg',img[:,:,2:3])

#merge chanel color
cv.imwrite('output/merge_chanel.jpg',cv.merge([b,r,g]))