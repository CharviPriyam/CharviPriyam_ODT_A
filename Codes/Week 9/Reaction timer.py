from machine import Pin
import time
import random

l=Pin(12,Pin.OUT)
pb=Pin(4,Pin.IN,Pin.PULL_UP)

while True:
    r=random.randrange(0,6)
    l.off()
    time.sleep(r)
    l.on()
    x=time.ticks_ms()
    while pb.value()==1:
        y=time.ticks_ms()
    l.off()
    t=time.ticks_diff(y,x)
    print(t)
    time.sleep(0.1)
