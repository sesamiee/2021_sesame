# 도 음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)
melody = [262, 294, 330, 349, 392, 440, 494, 523]
s = [4, 4, 5, 5, 4, 4, 3, 4]
#PWM 인스턴스 생성
#주파수 설정(4옥타프 도 음 : 262HZ)
pwm = GPIO.PWM(BUZZER_PIN,1)
pwm.start(10)

#time.sleep(2)
 #부저음이 나지 않음

#한 음계 소리 내기

try :
    for i in s :
        pwm.ChangeFrequency(melody[i])
        time.sleep(0.5)
        

    pwm.ChangeFrequency(melody[4])
    time.sleep(0.5)
    pwm.ChangeFrequency(melody[2])
    time.sleep(0.5)
    pwm.ChangeFrequency(melody[2])
    time.sleep(0.5)
    pwm.ChangeFrequency(melody[1])
    time.sleep(0.5)
   
    for i in s :
        pwm.ChangeFrequency(melody[i])
        time.sleep(0.5)
    
    pwm.ChangeFrequency(melody[2])
    time.sleep(0.5)
    pwm.ChangeFrequency(melody[1])
    time.sleep(0.5)
    pwm.ChangeFrequency(melody[2])
    time.sleep(0.5)
    pwm.ChangeFrequency(melody[0])
    time.sleep(0.5)




finally : 
    pwm.stop()
    GPIO.cleanup()