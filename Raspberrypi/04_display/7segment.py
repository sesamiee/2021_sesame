import RPi.GPIO as GPIO
import time

SEGMENT_PINS = [2,3,4,5,6,7,8] # A B C D E F G

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS : 
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment,GPIO.LOW)
    
#common cathode : ON -> HIGH OFF -> LOW
data = [1, 1, 1, 1, 1, 1, 0]

try : 
    for _ in range(3): #3번 반복
        for i in range(7) : 
            GPIO.output(SEGMENT_PINS[i], data[i])

        time.sleep(1)

        for i in range(7) : 
            GPIO.output(SEGMENT_PINS[i], GPIO.LOW)
        
        time.sleep(1)

finally : 
    GPIO.cleanup()
    print("clean and exit")

