from machine import Pin,PWM
import time

p=PWM(Pin(4))
p.freq(50)

while True:
    for x in range(40,110):
        p.duty(x)
        time.sleep(0.005)

#Motor duty cycle loop using range (smooth)
        
