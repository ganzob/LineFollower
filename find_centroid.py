from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as gpio
import time
import cv2
import numpy as np


camera=PiCamera()
camera.resolution=(160,120)
camera.framerate=32

rawCapture=PiRGBArray(camera,size=(160,120))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):

    img=rawCapture.array
    image_line=np.copy(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a,img_bw=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    M=cv2.moments(img_bw)

    cX=int(M["m10"]/ M["m00"])
    cY=int(M["m01"]/ M["m00"])

    cv2.circle(img,(cX,cY),5,(255,0,0),-1)
    cv2.imshow("Image",img_bw)
    cv2.imshow('hj',img)
    key=cv2.waitKey(1) & 0xFF
    #plt.show()
    rawCapture.truncate(0)

    if key==ord("q"):
        break

    

