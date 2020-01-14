from machine import KEY, Music, PIN, Timer, LED
import utime

bpm = 60

MIN_BPM = 60
MAX_BPM = 200

beats_per_ticks = [0,2,3,4,6]
bpt_pointer = 1

buzzer = Music()
a_key = KEY(0)
b_key = KEY(1)
c_key = KEY(2)
d_key = KEY(3)

led1 = LED(1)
led2 = LED(2)
led3 = LED(3)

def get_bpm_to_ms_count():
    return int(60000.0/bpm)

cur_time = 0

beats_per_tick = 4
beat_count = beats_per_ticks[bpt_pointer]

def decrease_beat_count(t):
    led2.toggle()
    global bpt_pointer
    global beat_count
    if bpt_pointer > 0:
        bpt_pointer -= 1
        beat_count -= 1

def increase_beat_count(t):
    led2.toggle()
    global bpt_pointer
    global beat_count
    if(bpt_pointer < beats_per_ticks.len()-1)
        bpt_pointer += 1
        beat_count += 1

c_key.irq(trigger=PIN.IRQ_FALLING, handler=decrease_beat_count)
d_key.irq(trigger=PIN.IRQ_FALLING, handler=increase_beat_count)

times_to_ms_count = get_bpm_to_ms_count()
next_beat_time = cur_time + times_to_ms_count

beats_to_add = 0;

def decrease_beat(t):
    global beats_to_add
    if bpm > MIN_BPM:
        beats_to_add -= 1
def increase_beat(t):
    global beats_to_add
    if bpm < MAX_BPM:
        beats_to_add += 1

a_key.irq(trigger=PIN.IRQ_FALLING, handler=decrease_beat)
b_key.irq(trigger=PIN.IRQ_FALLING, handler=increase_beat)

def tick():
    global beat_count
    beat_count -= 1
    if beat_count <= 0:
        led1.toggle()
        led3.off()
        buzzer.pitch(440, 50, 0)
        beat_count = beats_per_ticks[bpt_pointer]
    else:
        led3.toggle()
        led1.off()
        buzzer.pitch(262, 50, 0)

def handle_timer(t):
    global cur_time
    cur_time += 1

timer = Timer(1, mode=Timer.PERIODIC)
timer_a = timer.channel(Timer.CH_0, freq=1000)
timer_a.irq(trigger=Timer.TIMEOUT, handler=handle_timer)

print("BPM:", bpm)
print("times to count", times_to_ms_count)

while(True):
    bpm += beats_to_add
    times_to_ms_count = 60000.0/bpm
    beats_to_add = 0
    if next_beat_time <= cur_time:
        tick()
        next_beat_time += times_to_ms_count
