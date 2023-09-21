from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as gpio
import time
import cv2
import numpy as np
from operations import skeleton,findlength,findangle,median
from matplotlib import pyplot as plt
camera=PiCamera()
camera.resolution=(160,120)
camera.framerate=32

rawCapture=PiRGBArray(camera,size=(160,120))
j=0
mean_angle=0
angle=0
time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):

    img=rawCapture.array
    image_line=np.copy(img)
    gray=cv2.cvtColor(image_line,cv2.COLOR_RGB2GRAY)
    a,img_bw=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #img_bw=~img_bw
    img_skel=skeleton(img_bw)
    lines=cv2.HoughLinesP(img_skel,1,np.pi/180,80,minLineLength=30,maxLineGap=20)
    if(lines is not None):
        lines_all=np.copy(lines)
        if(lines.shape[0]>5):
       	     b=5
        else:
            b=lines.shape[0]
        print('b=',b)
        points=np.zeros([b,4])
        length=findlength(lines_all)
        w=np.transpose(length)
        max_index=np.argsort(w)[0,-b:]
        angle=0
        #max_index=max_index(0,4:7)
        for i in max_index:
            temp=lines_all[i]
            x1,y1,x2,y2=temp[0,:]
            print('x1:',x1,y1,x2,y2)      
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            c=findangle(x1=x1,y1=y1,x2=x2,y2=y2)
            print(c)
            angle+=c            
        print('angle:',angle)
        mean_angle=angle/max_index.shape[0]
        angle=median(mean_angle)
        print('mean_angle:',mean_angle)  
        print('mean:',angle)
    plt.scatter(j,angle)
    j=j+1    

    cv2.imshow('fd',img)
    key=cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key==ord("q"):
        print('j=',j)
        plt.show()
        break
     

