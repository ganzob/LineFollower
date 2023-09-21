import RPi.GPIO as GPIO
import time

def control_motor(motor,direction,speed):
    if(motor==1):
        if(direction=='forward'):
            a="1_a"
            b="1_b"
        else:
            a="1_b"
            b="1_a"
    else:
        if(direction=='forward'):
            a="2_a"
            b="2_b"
        else:
            a="2_b"
            b="2_a"
    pwms[a].ChangeDutyCycle(speed)
    pwms[b].ChangeDutyCycle(0)
	
