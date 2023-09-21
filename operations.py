import cv2
import numpy as np
from math import atan,pi
element=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
def skeleton(img):
    done=False
    skel=np.zeros_like(img)
    while(not done):
        eroded=cv2.erode(img,element)
        tmp=cv2.dilate(eroded,element)
        tmp=cv2.subtract(img,tmp)
        skel=cv2.bitwise_or(skel,tmp)
        img=eroded.copy()        
      
        if cv2.countNonZero(img)==0:
            done=True
    return skel
def findlength(a):
    length=np.sqrt(np.square(a[:,:,0]-a[:,:,2])+np.square(a[:,:,1]-a[:,:,3]))
    return length
def findangle(x1,y1,x2,y2,e=1e-6):
    return atan((x1-x2)/((y1-y2)+e))
b=np.zeros(5)
def median(a):
    b[4]=b[3]
    b[3]=b[2]
    b[2]=b[1]
    b[1]=b[0]
    b[0]=a
    #print(b)
    return b[np.argsort(b)[2]]
    
