import RPi.GPIO as GPIO
import time

TRIGGER_PIN  = 4
ECHO_PIN = 14
SERVO_MOTOR_FIN = 4
LED_PIN = 4
SWITCH_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SERVO_MOTOR_FIN, GPIO.OUT)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm = GPIO.PWM(SERVO_MOTOR_FIN, 50)
pwm.start(7.5)

try : 
    while True : 
            GPIO.output(TRIGGER_PIN, GPIO.HIGH)
            time.sleep(0.00001) # 10us (1us -> 0.000001s)
            GPIO.output(TRIGGER_PIN, GPIO.LOW)
            
            while GPIO.input(ECHO_PIN) == 0 :
                pass
            start = time.time()

            while GPIO.input(ECHO_PIN) == 1 :
                pass
            stop = time.time()
            duration_time = stop - start
            distance = 17160 * duration_time

            print('distance : %0.1fcm' % distance)
            
            if (distance <= 20) :
               while True :
                    GPIO.output(LED_PIN, GPIO.HGIH)
                    pwm.ChangeDutyCycle(10)
                    val = GPIO.input(SWITCH_PIN)

                    if val : 
                        GPIO.output(LED_PIN, GPIO.LOW)
                        pwm.ChangeDutyCycle(7.5)
                        time.sleep(0.1)
                        break

    
        



finally : 
    GPIO.cleanup()
    print('cleanup and out')