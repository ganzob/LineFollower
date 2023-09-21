from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import numpy as np
from dc_motor import *
from line_detection import setup_camera, line_detect
from matplotlib import pyplot as plt
time.sleep(0.1)
resolution_a=160
resolution_b=120
frame_rate=32
camera=PiCamera()
camera.resolution=(resolution_a,resolution_b)
camera.framerate=frame_rate

rawCapture=PiRGBArray(camera,size=(resolution_a,resolution_b))


# Motor configuration
motor_1_a=13
motor_1_b=15
motor_2_a=16
motor_2_b=18
motor_pwm_frequency=40
motor=dc_motor(motor_1_a,motor_1_b,motor_2_a,motor_2_b,motor_pwm_frequency)
motor.setup()

kp=2
ki=0
kd=0
ks=0.08
#motor.control_motor(1,'forward',100)
#motor.control_motor(2,'forward',100)
v=0.1
r=0.07
angle=0
angle_old=0
c=120
d=40
i=0
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):

    img=rawCapture.array
    angle,bias=line_detect(img)    
    w=kp*angle+kd*(angle-angle_old)-ks*(bias-80)
    #plt.scatter(i,angle) 
    i=i+1
    angle_old=angle
    speed_left=(2*v-w*r)/2
    speed_right=(2*v+w*r)/2
    pwm_left=speed_left*c+d
    pwm_right=speed_right*c+d
    pwm_right=pwm_right+5
    pwm_left=pwm_left-10
    if(pwm_left<0):
        #pwm_right=pwm_right+pwm_left
        pwm_left=0
    elif(pwm_left>100):
        pwm_left=100
    if(pwm_right<0):
        #pwm_left=pwm_left+pwm_right
        pwm_right=0
    elif(pwm_right>100):
        pwm_right=100
    print('speed:',w,pwm_left,pwm_right) 
 #   print('speed:',w,speed_left,speed_right,pwm_left, pwm_right)
    key=cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    motor.control_motor(1,'forward',pwm_left)
    motor.control_motor(2,'forward',pwm_right)
    if key==ord("q"):
        #plt.show()
        break
     

