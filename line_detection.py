from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
from operations import skeleton,findlength,findangle,median
from matplotlib import pyplot as plt

j=0
mean_angle=0
bias=0
def setup_camera(resolution_a,resolution_b,frame_rate):
    camera=PiCamera()
    camera.resolution=(resolution_a,resolution_b)
    camera.framerate=frame_rate

    rawCapture=PiRGBArray(camera,size=(resolutio_a,resolution_b))
def line_detect(img):
    angle=0
    bias=0
    img_temp=np.copy(img)
    image_line=np.copy(img)
    gray=cv2.cvtColor(image_line,cv2.COLOR_RGB2GRAY)
    a,img_bw=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
    img_bw=img_bw
    #print('thresh:',a)
    #img_skel=img_bw
    img_skel=skeleton(img_bw)
    lines=cv2.HoughLinesP(img_skel,1,np.pi/180,40,minLineLength=10,maxLineGap=3)
    if(lines is not None):
        lines_all=np.copy(lines)
        if(lines.shape[0]>8):
       	     b=8
        else:
            b=lines.shape[0]
        points=np.zeros([b,4])
        length=findlength(lines_all)
        w=np.transpose(length)
        max_index=np.argsort(w)[0,-b:]
        coordinates=lines_all[0]
        for i in max_index:
            temp=lines_all[i]
            x1,y1,x2,y2=temp[0,:]
            cv2.line(img_temp,(x1,y1),(x2,y2),(0,0,255),2)
            x1_sp,y1_sp,x2_sp,y2_sp=coordinates[0,:]
            if(max(y1_sp,y2_sp)<max(y1,y2)):
                coordinates=lines_all[i]
        #x1_sp,y1_sp,x2_sp,y2_sp=coordinates[0,:]
        #x1_sp,y1_sp,x2_sp,y2_sp=[0,20,140,100]  
        
        #print(x1_sp,y1_sp,x2_sp,y2_sp)
        #max(x1_sp
            #   print('x1:',x1,y1,x2,y2)      
        cv2.line(img, (x1_sp, y1_sp), (x2_sp, y2_sp), (255,255 , 0), 2)
        c=findangle(x1=x1_sp,y1=y1_sp,x2=x2_sp,y2=y2_sp)

        angle+=c            
        #print('angle:',angle)
        mean_angle=angle
        angle=median(mean_angle)
        #print('mean_angle:',mean_angle)  
        #print('mean:',angle)
        bias=(x1_sp+x2_sp)/2
        print(bias)
#    plt.scatter(j,angle)
#    j=j+1  
    cv2	.imshow('Skel',img_skel)  
    cv2.imshow('img',img)
    cv2.imshow('bw',img_bw)
    cv2.imshow('temp',img_temp)
    cv2.imshow('gray',gray)

    return angle,bias
