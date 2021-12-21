import RPi.GPIO as GPIO
import spidev
from lcd import drivers
import random

# 설정
SERVO_MOTOR_FIN_1 = 4
led_most_left = 26
led_left = 19
led_right = 13
led_most_right = 6
button = 27

#모드 설정하기
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_MOTOR_FIN_1,GPIO.OUT)
GPIO.setup(led_most_left,GPIO.OUT)
GPIO.setup(led_left,GPIO.OUT)
GPIO.setup(led_right,GPIO.OUT)
GPIO.setup(led_most_right,GPIO.OUT)
GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#서보모터 설정
pwm = GPIO.PWM(SERVO_MOTOR_FIN_1, 50)
pwm.start(7.5) # 0도

# SPI 인스턴트 생성
spi = spidev.SpiDev()
#SPI 통신 시작
spi.open(0,0) #bus: 0, dev: 0
#SPI 통신 속도 설정
spi.max_speed_hz = 100000 #최대 속도
# 채녈에서 SPI 데이터 읽기 (0 ~ 1023)
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_2 : channel config (channel 0) (+8) -> 0000 1000 -> 1000 0000
  ret = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out

display = drivers.Lcd() #lcd 설정

def main_process() : #가장 핵심적인 프로세스
    display.lcd_clear() # 화면 초기화
    score = 0
    time = 0
    led_check = 0
    while True :
        if(led_check == 0) : #LED가 모두 꺼져있을 때
            led_num = random.randrange(1,5) #랜덤으로 하나 키기
            led_check = 1 # lED가 켜져있음을 나타내기
            if(led_num == 1) : GPIO.output(led_most_left,GPIO.HIGH)
            elif(led_num == 2) : GPIO.output(led_left,GPIO.HIGH) 
            elif(led_num == 3) : GPIO.output(led_right,GPIO.HIGH) 
            elif(led_num == 4) : GPIO.output(led_most_right,GPIO.HIGH) 

       
        reading_al = analog_read(1) #아날로그 값(가변저항 값)읽기
        gak = (5/1023)*reading_al + 5 #가변저항값을 pwm으로 변환
        print("reading = %f" % gak)
        pwm.ChangeDutyCycle(gak)
        
        if((led_num == 1 and gak == 10) or (led_num == 2 and (gak > 8.5 and gak < 8.7)) or (led_num == 3 and (gak >5.7 and gak < 6)) or (led_num == 4 and gak < 5.1)) :
            #켜진 LED에 망치가 이동했을 때 
            score += 1
            led_check = 0 #LED가 모두 꺼짐을 알림
            GPIO.output(led_most_right,GPIO.LOW) 
            GPIO.output(led_right,GPIO.LOW)
            GPIO.output(led_left,GPIO.LOW)
            GPIO.output(led_most_left,GPIO.LOW)

        # lcd 내용출력
        real_time = time/10 #시간 데이터를 실제시간과 맞게 변환
        display.lcd_display_string("score = %d" % score,1)
        display.lcd_display_string("time = %1.1f" % real_time,2)
        time += 1
        if(score >= 20) : break
    display.lcd_clear()
    display.lcd_display_string("your time = %1.1f" % real_time,1)
    display.lcd_display_string("Press to start",2)

try :
    main_process()
    while True :
        val = GPIO.input(button)
        if(val == 0) : #버튼이 눌린상태라면 다시 게임실행
            main_process() 
        
finally : 
    spi.close()
    GPIO.cleanup()
    display.lcd_clear()