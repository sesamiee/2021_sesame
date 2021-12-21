import RPi.GPIO as GPIO
import time

BUZZER_PIN = 5
LED_PIN = 6
SWITCH_PIN = 13
PIR_PIN = 19
count = 0
secound = 0.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIR_PIN, GPIO.IN)

PWM = GPIO.PWM(BUZZER_PIN, 1)
PWM.start(0)

GPIO.output(LED_PIN,GPIO.LOW)
time.sleep(5)
print("PIR is ready...")

try :
    while True : 
        val = GPIO.input(PIR_PIN)                     # PIR센서를 이용해 사람 감지
        if val == 1 :                                 # 사람을 감지 했을 때 실행 
            print('움직임 감지')
            PWM.ChangeDutyCycle(10)
            while True :                              # 사람을 감지 했을 때 특정 조건을 만족할 때 까지 무한반복
                GPIO.output(LED_PIN, GPIO.HIGH)       # LED 켜기
                figure = GPIO.input(SWITCH_PIN)       
                for i in range(262, 524) :            # 부저를 낮은 도 부터 높은 도 까지 순서대로 올리기
                    PWM.ChangeFrequency(i)
                    time.sleep(0.001)
                    secound = secound + 0.001

                for i in range(523, 262, -1) :        # 부저를 높은 도 부터 낮은 도 까지 순서대로 내리기
                    PWM.ChangeFrequency(i)
                    time.sleep(0.001)
                    secound = secound + 0.001

                if figure :                           # 스위치를 누르고 있었을 경우
                    count = count + 1                 # 1초 누적하기 
                    time.sleep(0.478)                 # 1초를 맞추기 위해 사용
                    secound = 0.0
                else : 
                    count = 0                         # 스위치를 누르고 있지 않았을 경우 누적한 시간 초기화 하기

                if count == 10 :                      # 스위치를 10초동안 누르고 있었다면 경보 해제 
                    GPIO.output(LED_PIN,GPIO.LOW)     # LED 끄기 
                    print("해제")
                    PWM.ChangeDutyCycle(0)            # 부저 끄기 
                    break                             # 나가기 

        else : 
            print('움직임 없음')

        time.sleep(1)

    
            

finally :
    GPIO.cleanup()
    print('cleanup and out')