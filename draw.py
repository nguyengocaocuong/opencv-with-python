import cv2 as cv 
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
cv.rectangle(blank,(0,0),(100,100),(123,232,123),-1)
cv.circle(blank,(170,170),90,(123,232,123),-1)
cv.line(blank,(0,0),(170,170),(100,100,100),4)
cv.imwrite('output.jpg',blank)