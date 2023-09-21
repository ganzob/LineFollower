import RPi.GPIO as GPIO
import time


encoder_1_a=31
encoder_1_b=33
encoder_2_a=35
encoder_2_b=37

GPIO.setup(encoder_1_a,GPIO.IN)
GPIO.setup(encoder_1_b,GPIO.IN)
GPIO.setup(encoder_2_a,GPIO.IN)
GPIO.setup(encoder_2_b,GPIO.IN)
motor_1=0
motor_2=0
def motor_1(channel):
    if(GPIO.input(encoder_1_b)=='HIGH'):
        motor_1++
    else:
        motor_1--
def motor_2(channel):
    if(GPIO.input(encoder_2_b)=='HIGH'):
        motor_2++
    else:
        motor_2--

GPIO.add_event_detect(encoder_1_a,GPIO.RISING, callback=motor_1)
GPIO.add_event_detect(encoder_2_a,GPIO.RISING, callback=motor_2)


