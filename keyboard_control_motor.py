from dc_motor import *
import time
#from pynput import keyboard
import curses

screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

motor_1_a=15
motor_1_b=13
motor_2_a=18
motor_2_b=16
motor_pwm_frequency=40
motor=dc_motor(motor_1_a,motor_1_b,motor_2_a,motor_2_b,motor_pwm_frequency)
motor.setup()

#def on_press(key):
#    try:k=key.char
#    except:k=key.name
#    if(key==keyboard.Key.esc): return False
#lis=keyboard.Listener(on_press=on_press)
#lis.start()
#lis.join()  
try:
    while True:
        input=screen.getch()
        print(input)
        if input==ord('q'):
            break
        elif input==curses.KEY_UP:
            print("W")
            motor.control_motor(1,'forward',100)
            motor.control_motor(2,'forward',100)
        elif input==curses.KEY_DOWN:
            print("S")
            motor.control_motor(1,'reverse',40)
            motor.control_motor(2,'reverse',40)
        elif input==curses.KEY_RIGHT:
            motor.control_motor(1,'forward',30)
            motor.control_motor(2,'reverse',30)
        elif input==curses.KEY_LEFT:
            print("A")
            motor.control_motor(1,'reverse',30)
            motor.control_motor(2,'forward',30)
        elif input==ord(' '):
            motor.control_motor(1,'forward',0)
            motor.control_motor(2,'forward',0)
        #time.sleep(0.2)
        else:
            motor.control_motor(1,'forward',0)
            motor.control_motor(2,'forward',0)
           
finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()

