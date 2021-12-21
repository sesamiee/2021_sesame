# 도 음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

#PWM 인스턴스 생성
#주파수 설정(4옥타프 도 음 : 262HZ)
PWM = GPIO.PWM(BUZZER_PIN, 262)
PWM.start(50)

time.sleep(2)
PWM.ChangeDutyCycle(0) #부저음이 나지 않음

#한 음계 소리 내기
melody = [262, 294, 330, 349, 392, 440, 494, 523]
try :
    for i in melody :
        PWM.ChangeFrequency(i)
        time.sleep(1)


finally : 
    PWM.stop()
    GPIO.cleanup()