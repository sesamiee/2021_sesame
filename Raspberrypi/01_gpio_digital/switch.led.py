import RPi.GPIO as GPIO

LED_PIN = 4
SWITCH_PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항

try :
    while True:
        val = GPIO.input(SWITCH_PIN) #누르지 않으면 0,누르면 1
        print(val)
        GPIO.output(LED_PIN, val) #val이 0 또는 1임으로 굳이 함수를 쓸필요가 없다

finally:
    GPIO.cleanup()
    print("clean and out")

