from machine import Pin,PWM
import time

p=PWM(Pin(4))
p.freq(50)
l=[35,55,75,95]

while True:
    for x in l:
        p.duty(x)
        time.sleep(0.1)

#Motor duty cycle loop using list
        
