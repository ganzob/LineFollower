from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as gpio
import time
import cv2
import numpy as np
#from matplotlib import pyplot as plt
from math import atan,pi
camera=PiCamera()
camera.resolution=(160,120)
camera.framerate=32

rawCapture=PiRGBArray(camera,size=(160,120))

time.sleep(0.1)
element=cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
#print("size",size)
def skeleton(img):
    done=False
    skel=np.zeros(img.shape,np.uint8)
    size=np.size(img)
    #eroded=img
    #for i in range(40):
    #    eroded=cv2.erode(eroded,element)
    #print(size)
    while(not done):
        eroded=cv2.erode(img,element)
        tmp=cv2.dilate(eroded,element)
        tmp=cv2.subtract(img,tmp)
        skel=cv2.bitwise_or(skel,tmp)
        img=eroded.copy()
        
        zeros=size-cv2.countNonZero(img)
        if zeros==size:
            done=True
    print('a')
    return skel
def findlength(a):
    length=np.sqrt(np.square(a[:,:,0]-a[:,:,2])+np.square(a[:,:,1]-a[:,:,3]))
    #print('lenth:',length.shape)
    return length
def findangle(x1,y1,x2,y2,e=1e-6):
    return atan((x1-x2)/((y1-y2)+e))*180/pi
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):

    img=rawCapture.array
    image_line=np.copy(img)
    #canny=canny(image_line)
    gray=cv2.cvtColor(image_line,cv2.COLOR_RGB2GRAY)
    #print("gray:",gray.shape)
    #blur=cv2.GaussianBlur(gray,(5,5),0)
    
    #print("skel:",skel.shape) 
    #img_bw=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    a,img_bw=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #img_bw=~img_bw
    #cv2.imshow('fd',img_bw)
    skel=skeleton(img_bw)
    #rawCapture.truncate(0)
    #canny=img_bw
    #print(img_bw)
    #canny=cv2.Canny(img_bw,150,200)
    #slines=None
    #canny=cv2.dilate(canny,element) 
    lines=cv2.HoughLinesP(img_bw,90,np.pi/90,200,minLineLength=50,maxLineGap=10)
    #line_image=disp_lines(image_line,lines)
    #plt.subplot(1,1,1),plt.imshow(img_bw)

    #print(lines.shape)
    if(lines is not None):
        #print(lines.shape[0])
        lines_all=np.copy(lines)
        if(lines.shape[0]>5):
       	     b=5
        else:
            b=lines.shape[0]
        max=0
        #print('b:',b)
        points=np.zeros([b,4])
        #for line in lines_all:
        #    x1, y1, x2, y2 = line[0]
        #print(lines_all.shape)
        length=findlength(lines_all)
        #print('length:',length.shape)
        w=np.transpose(length)
        max_index=np.argsort(w)[0,-b:]
        #print('M:',max_index.shape)
        #print('max_index:',max_index)
        #print(lines_all.shape)
        for i in (max_index):
            temp=lines_all[i]
         #   print(lines_all[i])
            #print('shape:',lines_all[i].shape)
            x1,y1,x2,y2=temp[0,:]      
            #print(lines_all[max_index[i],0,:])
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            #angle=findangle(x1,
    cv2.imshow('fd',skel)
    #print(type(img_bw))
    key= cv2.waitKey(1)&0xFF
    #plt.show()
    rawCapture.truncate(0)

    if key==ord("q"):
        break


