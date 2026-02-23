#capacitive touch to LEDs (3)
from machine import Pin,PWM
import time

r=Pin(32,Pin.IN,Pin.PULL_UP)
l1=PWM(Pin(12,Pin.OUT))
l2=PWM(Pin(14,Pin.OUT))
l3=PWM(Pin(27,Pin.OUT))
l1.freq(500)
l2.freq(500)
l3.freq(500)


while True:
    r_val=r.value()
    print(r_val)
    time.sleep(0.2)
    if r_val==0:
       l1.duty(1023)
       l2.duty(1023)
       l3.duty(1023)
       time.sleep(0.05)
       l1.duty(0)
       l2.duty(0)
       l3.duty(0)
       time.sleep(0.05)
            

    
