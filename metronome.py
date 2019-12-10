from machine import KEY, Music, PIN, Timer, LED
import utime

buzzer = Music()
a_key = KEY(0)
b_key = KEY(1)

bpm = 60

led1 = LED(1)
led2 = LED(2)
led3 = LED(3)

def get_bpm_to_ms_count():
    return int(60000/bpm)

times_to_count = get_bpm_to_ms_count()
ms_count = times_to_count

times_to_beat_count = 4;
beat_count = times_to_beat_count

def handle_keys():
    global bpm
    global times_to_count
    if a_key.value() == 0 and bpm > 40:
        bpm -= 1
        times_to_count = get_bpm_to_ms_count()
        led1.toggle()
    if b_key.value() == 0 and bpm < 200:
        bpm += 1
        times_to_count = get_bpm_to_ms_count()
        led1.toggle()

def handle_minus_key():
    global bpm
    global times_to_count
    if bpm > 40:
        bpm -= 1
        times_to_count = get_bpm_to_ms_count()
        led2.toggle()

def handle_add_key():
    global bpm
    global times_to_count
    if bpm < 200:
        bpm += 1
        times_to_count = get_bpm_to_ms_count()
        led2.toggle()

def beat():
    global beat_count
    beat_count -= 1
    if beat_count == 0:
        led1.toggle()
        led3.off()
        #buzzer.play('D')
        beat_count = times_to_beat_count
    else:
        led3.toggle()
        led1.off()
        #buzzer.play('C')

def flash_led(led):
    led.on()
    utime.sleep_ms(10)
    led.off()

def handle_timer(t):
    global ms_count
    ms_count -= 1
    if(ms_count == 0):
        beat()
        ms_count = times_to_count

print("BPM:", bpm)
print("times to count", times_to_count)

timer = Timer(1, mode=Timer.PERIODIC)
timer_a = timer.channel(Timer.CH_0, freq=1000)
timer_a.irq(trigger=Timer.TIMEOUT, handler=handle_timer)

a_key.irq(PIN.IRQ_FALLING, handle_minus_key)
b_key.irq(PIN.IRQ_FALLING, handle_add_key)
