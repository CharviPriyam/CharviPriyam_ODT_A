#REED to buzzers (2) [PAW FINAL][HAPPY]
from machine import Pin,PWM
import time

r=Pin(32,Pin.IN,Pin.PULL_UP)
b=PWM(Pin(5,Pin.OUT))

while True:
    r_val=r.value()
    print(r_val)
    time.sleep(0.2)
    if r_val==0:
        b.duty(512)
        for x in range(2000,2100,1):
            b.freq(x)
            time.sleep(0.001)
        
    else:
        b.duty(0)

    



