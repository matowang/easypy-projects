from machine import PIN
from enum import Enum
class Common(enum):
  ANODE = 0
  CATHODE = 1

class SevenSeg:

  str_ecoding = {
    '0': (1, 1, 1, 1, 1, 1, 0),
    '1': (0, 1, 1, 0, 0, 0, 0)
  }

  def __init__(self, A, B, C, D, E, F, G, DP, common, power):  
    self.common = common
    self.off_value = 0 if common == Common.CATHODE else 1
    self.on_value = 1 if common == Common.CATHODE else 0
    init_value = self.off_value
    
    self.PINS = {A,B,C,D,E,F,G}
    
    for pin in self.PINS:
      pin = PIN(
        id='P' + pin, 
        mode=PIN.OUT, 
        value=init_value, 
        drive=power)
        
  def on_all(self):
    for pin in self.PINS.values():
      pin.value(self.on_value)
      
  def off_all(self):
    for pin in self.PINS.values():
      pin.value(self.off_value)
      
  def light_segs(self, A,B,C,D,E,F,G):
    input = {A,B,C,D,E,F,G}
    for i in range(7):
      if input[i]:
        self.PINS[i].value(on_value)
      else:
        self.PINS[i].value(off_value)
  
  def draw(s):
    code = SevenSeg.str_encoding[s]
    self.light_segs(code)
