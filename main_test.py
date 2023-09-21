from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import numpy as np
from dc_motor import *

camera=PiCamera()
camera.resolution=(480,640)
camera.framerate=90

rawCapture=PiRGBArray(camera,size=(480,640))

time.sleep(0.1)

motor_1_a=15
motor_1_b=13
motor_2_a=18
motor_2_b=16
motor_pwm_frequency=40
motor=dc_motor(motor_1_a,motor_1_b,motor_2_a,motor_2_b,motor_pwm_frequency)
motor.setup()
direction='reverse'

    
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):

    img=rawCapture.array
    image_line=np.copy(img)
    #canny=canny(image_line)
    gray=cv2.cvtColor(image_line,cv2.COLOR_RGB2GRAY)
    
    blur=cv2.GaussianBlur(gray,(5,5),0)
    a,img_bw=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #canny=img_bw
    #print(img_bw)
    canny=cv2.Canny(img_bw,150,200)
    lines=None
    lines=cv2.HoughLinesP(canny,60,np.pi/360,60,np.array([]),minLineLength=100,maxLineGap=60)
    #line_image=disp_lines(image_line,lines)
    #plt.subplot(1,1,1),plt.imshow(img_bw)
    #print(lines.shape)
    if(lines is not None):
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(gray, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.imshow('fd',gray)
    #print(type(img_bw))
    key=cv2.waitKey(1) & 0xFF
    #plt.show()
    rawCapture.truncate(0)

    motor.control_motor(1,'reverse',20)
    motor.control_motor(2,'forward',20)
    if key==ord("q"):
        break


    
