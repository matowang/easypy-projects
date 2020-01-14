# Write your code here :-)
from seven_seg import SevenSeg, Common
sev_seg = SevenSeg(14, 13, 20, 16, 15, 2, 8, 19, Common.ANODE)

for i in range(10):
    sev_seg.draw(i)
