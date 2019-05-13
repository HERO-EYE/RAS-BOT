import RPi.GPIO as GPIO
from time import sleep
from Bluetin_Echo import Echo
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIGGER_PIN = 12
ECHO_PIN = 16
m1 = [26 , 19]
m2 = [13 , 6]
sPin = [21 , 20]
servo = []
speed_of_sound = 315
echo = Echo(TRIGGER_PIN, ECHO_PIN, speed_of_sound)
samples = 5

for i in range(2):
    GPIO.setup(m1[i] , GPIO.OUT)
    GPIO.setup(m2[i] , GPIO.OUT)
    GPIO.setup(sPin[i] , GPIO.OUT)
    servo.append(GPIO.PWM(sPin[i], 30))
    servo[i].start(0)

def forward():
    GPIO.output(m1[0], 1)
    GPIO.output(m1[1], 0)
    GPIO.output(m2[0], 1)
    GPIO.output(m2[1], 0)

def backward():
    GPIO.output(m1[0], 0)
    GPIO.output(m1[1], 1)
    GPIO.output(m2[0], 0)
    GPIO.output(m2[1], 1)

def left():
    GPIO.output(m1[0], 1)
    GPIO.output(m1[1], 0)
    GPIO.output(m2[0], 0)
    GPIO.output(m2[1], 1)

def right():
    GPIO.output(m1[0], 0)
    GPIO.output(m1[1], 1)
    GPIO.output(m2[0], 1)
    GPIO.output(m2[1], 0)

def stop():
    GPIO.output(m1[0], 0)
    GPIO.output(m1[1], 0)
    GPIO.output(m2[0], 0)
    GPIO.output(m2[1], 0)

def Servo(ser , a):
    v = (12.5/180.0)*a
    ser.ChangeDutyCycle(v)

def ultrasonic():
    global echo
    global samples
    result = echo.read('cm', samples)
    print(result, 'cm')
    return result
    
def motor_test():
    stop()
    forward()
    sleep(2)
    stop()
    sleep(1)
    backward()
    sleep(2)
    stop()
    sleep(1)
    left()
    sleep(2)
    stop()
    sleep(1)
    right()
    sleep(2)
    stop()
    sleep(1)

def servo_test():
    for n in range(45 , 160):
        Servo(servo[1] , n)
        sleep(0.02)
    for n in range(10 , 180):
        Servo(servo[0] , n)
        sleep(0.02)

while True:
    try:
        forward()
        d = ultrasonic()
        if (d < 15):
            backward()
            sleep(1)
            left()
            sleep(1)
    except KeyboardInterrupt:
        print("Ok ok, quitting")
        stop()
        sys.exit(1)
    
    #sleep(0.7)