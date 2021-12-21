import RPi.GPIO as GPIO
import time

LED_red = 26
LED_yellow = 6
LED_blue = 19
LED_green = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_red, GPIO.OUT)
GPIO.setup(LED_yellow, GPIO.OUT)
GPIO.setup(LED_green, GPIO.OUT)
GPIO.setup(LED_blue, GPIO.OUT)


GPIO.output(LED_red, GPIO.HIGH) 
print("led red on")
time.sleep(2)
GPIO.output(LED_red, GPIO.LOW)
GPIO.output(LED_yellow, GPIO.HIGH)
print("led yellow on")
time.sleep(2)
GPIO.output(LED_yellow, GPIO.LOW)
GPIO.output(LED_green, GPIO.HIGH)
print("led green on")
time.sleep(2)
GPIO.output(LED_green, GPIO.LOW)
GPIO.output(LED_blue, GPIO.HIGH)
print("led blue on")
time.sleep(2)
GPIO.output(LED_blue, GPIO.LOW)

  

GPIO.cleanup()
GPIO.setup(LED_red, GPIO.IN)
GPIO.setup(LED_yellow, GPIO.IN)
GPIO.setup(LED_green, GPIO.IN)