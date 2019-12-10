from machine import KEY, Music, PIN, Timer, LED

led1 = LED(1)

def handle_timer():
    led1.toggle()

timer = Timer(1, mode=Timer.PERIODIC)
timer_a = timer.channel(0, freq=1)
timer_a.irq(trigger=Timer.TIMEOUT, handler=handle_timer)
