import RPi.GPIO as GPIO
import time

LED_FIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_FIN,GPIO.OUT)

pwm = GPIO.PWM(LED_FIN, 50) # 사용할핀 , 주파수설정 (초당 사이클 반복 횟수)
pwm.start(0) # 0 ~ 100

try : 
    while True :
        #서서히 켜짐
        for i in range(0, 101, 5) :     #start, end, step
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
        # 서서히 꺼짐
        for i in range(100, -1, -5) :
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)

finally :
    pwm.stop()
    GPIO.cleanup()
    print("clean and out")