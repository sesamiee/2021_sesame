import RPi.GPIO as GPIO
import time

SERVO_MOTOR_FIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_MOTOR_FIN,GPIO.OUT)

# 서보모터 제어에 필요한 주파수 : 50hz
pwm = GPIO.PWM(SERVO_MOTOR_FIN, 50)
pwm.start(7.5) # 0도

# 1: 0도 2: -90도 3: 90도 9 exit
try : 
    while True : 
        val = input("1: 0도 2: -90도 3: 90도 9 exit")
        if val == '1':
            pwm.ChangeDutyCycle(7.5)
        elif val == 2 :
            pwm.ChangeDutyCycle(5)
        elif val == 3 :
            pwm.ChangeDutyCycle(10)
        elif val == 9 :
            break 
finally :
    pwm.stop()
    GPIO.cleanup()
    print("clean and out")