import RPi.GPIO as GPIO
import time

encoder_1_a=31
encoder_1_b=33
encoder_2_a=35
encoder_2_b=37
servo_1=21
servo_2=23
servo_frequency=50
GPIO.setup(encoder_1_a,GPIO.IN)
GPIO.setup(encoder_1_b,GPIO.IN)
GPIO.setup(encoder_2_a,GPIO.IN)
GPIO.setup(encoder_2_b,GPIO.IN)

GPIO.setup(servo_1,GPIO.OUT)
GPIO.setup(servo_2,GPIO.OUT)

servo_1_pwm=GPIO.PWM(servo_1,servo_frequency)
servo_2_pwm=GPIO.PWM(servo_2,servo_frequency)

servo_1_pwm.start(7.5)
time.sleep(1)
servo_1_pwm.start(10)
time.sleep(1)





