import RPi.GPIO as GPIO
import time
class dc_motor():
    
    def __init__(self,motor_1_a,motor_1_b,motor_2_a,motor_2_b,motor_pwm_frequency):
        self.motor_1_a=motor_1_a
        self.motor_1_b=motor_1_b
        self.motor_2_a=motor_2_a
        self.motor_2_b=motor_2_b
        self.motor_pwm_frequency=motor_pwm_frequency
        self.pwms={}
    def setup(self):
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.motor_1_a,GPIO.OUT)
        GPIO.setup(self.motor_1_b,GPIO.OUT)
        GPIO.setup(self.motor_2_a,GPIO.OUT)        
        GPIO.setup(self.motor_2_b,GPIO.OUT)
        self.pwms['1_a']=GPIO.PWM(self.motor_1_a,self.motor_pwm_frequency)
        self.pwms['1_b']=GPIO.PWM(self.motor_1_b,self.motor_pwm_frequency)
        self.pwms['2_a']=GPIO.PWM(self.motor_2_a,self.motor_pwm_frequency)
        self.pwms['2_b']=GPIO.PWM(self.motor_2_b,self.motor_pwm_frequency)
        self.pwms['1_a'].start(0)
        self.pwms['1_b'].start(0)
        self.pwms['2_a'].start(0)
        self.pwms['2_b'].start(0)
        
    def control_motor(self,motor=1,direction='forward',speed=0):
        if(motor==1):
            if(direction=='forward'):
                a='1_a'
                b='1_b'
            else:
                a='1_b'
                b='1_a'
        else:
            if(direction=='forward'):
                a='2_a'
                b='2_b'
            else:
                a='2_b'
                b='2_a'
        self.pwms[a].ChangeDutyCycle(speed)
        self.pwms[b].ChangeDutyCycle(0)
    def stop():
        for i in range(pwms):
            self.pwms[i].stop()
        

