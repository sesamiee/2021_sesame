import spidev
import time
import RPi.GPIO as GPIO

LED = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
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

try : 
    while True:
     
        reading = analog_read(0) # reading(0 ~ 1023)
        print("reading = %d" % reading)
        if (reading > 512) :
          GPIO.output(LED, GPIO.HIGH)
        
        if(reading < 512) : 
          GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)


finally : 
    spi.close()
