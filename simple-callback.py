from machine import KEY, PIN, LED

a_key = KEY(0)

led1 = LED(1)

def handle(t):
    print("hello")
    led1.toggle()

a_key.irq(PIN.IRQ_FALLING, handle)

print("initialized")
