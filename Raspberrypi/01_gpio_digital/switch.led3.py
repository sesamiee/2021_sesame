import RPi.GPIO as GPIO

LED_PIN_1 = 17
LED_PIN_2 = 27
LED_PIN_3 = 22
SWITCH_PIN_1 = 10
SWITCH_PIN_2 = 9
SWITCH_PIN_3 = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1,GPIO.OUT)
GPIO.setup(LED_PIN_2,GPIO.OUT)
GPIO.setup(LED_PIN_3,GPIO.OUT)
GPIO.setup(SWITCH_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항

try :
    while True:
        val = GPIO.input(SWITCH_PIN_1) #누르지 않으면 0,누르면 1
        print(val)
        GPIO.output(LED_PIN_1, val) #val이 0 또는 1임으로 굳이 함수를 쓸필요가 없다

        bal = GPIO.input(SWITCH_PIN_2) #누르지 않으면 0,누르면 1
        print(bal)
        GPIO.output(LED_PIN_2, bal)

        vel = GPIO.input(SWITCH_PIN_3) #누르지 않으면 0,누르면 1
        print(vel)
        GPIO.output(LED_PIN_3, vel)

finally:
    GPIO.cleanup()
    print("clean and out")

