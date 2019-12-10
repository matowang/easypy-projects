from machine import Timer
from machine import LED
import utime

led = LED(1)
while True:			        #当真的
    led.toggle()
    utime.sleep_ms (1000)	#延迟1000ms
