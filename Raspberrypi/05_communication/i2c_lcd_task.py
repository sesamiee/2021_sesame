from lcd import drivers
import time
import datetime
import Adafruit_DHT

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
DHT_PIN = 10

try :
    print("writing to display")
    while True :
        now = datetime.datetime.now()
        display.lcd_display_string((now.strftime("%x%X")),1)
        time.sleep(0.5)
        h,t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            display.lcd_display_string((f'H= {t:.1f}*,T: {h:.1f}%'),2)
        time.sleep(0.5)

finally :
    print("clean up")
    display.lcd_clear()

