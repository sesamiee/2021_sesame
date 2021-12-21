from lcd import drivers
import time

display = drivers.Lcd()


try :
    print("writing to display")
    display.lcd_display_string("wa sans!",1)
    while True :
        display.lcd_display_string(" you know this! ",2)
        time.sleep(2)
        display.lcd_display_string("It's s.o h.a.r.d",2)
        time.sleep(2)

finally :
    print("clean up")
    display.lcd_clear()

