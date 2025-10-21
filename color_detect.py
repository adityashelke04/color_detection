#HSV - Hue, Saturation, Value

import cv2
from PIL import Image
from util import get_limits


 
yellow = [0,255,255] #yellow color code - RGB colorspace
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)   #convert original color space to HSV

    lowerlimit, upperlimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerlimit, upperlimit)  #get the color range we want to detect

    mask_ = Image.fromarray(mask) #convert to pillow

    bbox = mask_.getbbox()       #get the bounding box - easy and best function
    #print(bbox) use this if u want to see the coords of the bounding box

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame,(x1,y1), (x2,y2), (0,255,0), 5)

    cv2.imshow("Color Detection",frame)
    key = cv2.waitKey(10)
    if key == 27:     #27 for esc key
        break

cap.release()

cv2.destroyAllWindows()