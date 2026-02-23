#CAPACITANCE to buzzers (2) [TAIL FINAL][ANGRY]
from machine import Pin,TouchPad,PWM
import time

t=TouchPad(Pin(4))
b=PWM(Pin(5,Pin.OUT))

while True:
    t_val=t.read()
    print(t_val)
    time.sleep(0.2)
    if t_val<200:
        for i in range(900,1400,1):
            b.freq(i)
            b.duty(600)
            time.sleep(0.001)
        for i in range(1400,1100,-1):
            b.freq(i)
            b.duty(512)
            time.sleep(0.001)
        for i in range(1100,1600,1):
            b.freq(i)
            b.duty(600)
            time.sleep(0.001)
        for i in range(1600,1200,-1):
            b.freq(i)
            b.duty(512)
            time.sleep(0.001)
    else:
        b.duty(0)

    




