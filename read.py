import cv2 as cv
import os
# img = cv.imread('Photos/cat.jpg')
# cv.imwrite('ouput.jpg',img)

capture = cv.VideoCapture('Videos/dog.mp4')
os.mkdir('frame')
index = 1
isTrue = True
while isTrue:
    isTrue, frame = capture.read()
    if isTrue:
        cv.imwrite("frame/{}.jpg".format(index),frame)
    index+=1
capture.release()
    
    