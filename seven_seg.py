from machine import PIN
class Common:
  ANODE = 0
  CATHODE = 1

class SevenSeg:
    str_encoding = {
        '0': (1, 1, 1, 1, 1, 1, 0),
        '1': (0, 1, 1, 0, 0, 0, 0),
        '2': (1, 1, 0, 1, 1, 0, 1),
        '3': (1, 1, 1, 1, 0, 0, 1),
        '4': (0, 1, 1, 0, 0, 1, 1),
        '5': (1, 0, 1, 1, 0, 1, 1),
        '6': (1, 0, 1, 1, 1, 1, 1),
        '7': (1, 1, 1, 0, 0, 0, 0),
        '8': (1, 1, 1, 1, 1, 1, 1),
        '9': (1, 1, 1, 1, 0, 1, 1),
        'A': (1, 1, 1, 0, 1, 1, 1),
    }
    def __init__(self, A, B, C, D, E, F, G, DP, common):
        self.common = common
        if common == Common.CATHODE:
            self.off_value = 0
            self.on_value = 1
        else:
            self.off_value = 1
            self.on_value = 0

        init_value = self.off_value

        self.PINS = [A,B,C,D,E,F,G,DP]

        for i in range(len(self.PINS)):
            print(i)
            self.PINS[i] = PIN('P{}'.format(self.PINS[i]))
            self.PINS[i].init(mode=PIN.OUT, value=init_value)

    def on_all(self):
        for pin in self.PINS:
            pin.value(self.on_value)

    def off_all(self):
        for pin in self.PINS:
            pin.value(self.off_value)

    def light_segs(self, A,B,C,D,E,F,G):
        input = [A,B,C,D,E,F,G]
        for i in range(7):
            if input[i]:
                self.PINS[i].value(self.on_value)
            else:
                self.PINS[i].value(self.off_value)

    def draw(self, s):
        code = SevenSeg.str_encoding[str(s)]
        print(*code)
        self.light_segs(*code)

    def dot_on(self):
        self.PINS[7].value(self.on_value)

    def dot_off(self):
        self.PINS[7].value(self.off_value)
