import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try : 
    while True :
        h,t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print(f'온도 ={t:.1f}*,습도 : {h:.1f}%')
        else : 
            print('readd err')
            time.sleep(0.1)

finally: 
    print('bye')
