# Write your code here :-)
from machine import Music, LED, KEY
import utime
RGB_NUM = 5
rgb = LED(LED.RGB)

try:
    while True:
        for r in range(1,256):
            for rgb_light in range(1, RGB_NUM+1):
                rgb.rgb_write(rgb_light, r, 0, 256-r)
        for r in range(1,256):
            for rgb_light in range(1, RGB_NUM+1):
                rgb.rgb_write(rgb_light, 256-r, r, 0)
        for r in range(1,256):
            for rgb_light in range(1, RGB_NUM+1):
                rgb.rgb_write(rgb_light, 0, 256-r, r)
        utime.sleep_ms(1)
finally:
    rgb.off()
