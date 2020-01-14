# Write your code here :-)
from seven_seg import SevenSeg, Common
import utime

sev_seg = SevenSeg(31, 45, 27, 29, 30, 44, 39, 28, Common.ANODE)

while(True):
    for i in range(10):
        sev_seg.draw(i)
        utime.sleep_ms(100)
        if i%2 == 0:
            sev_seg.dot_on()
        else:
            sev_seg.dot_off()

