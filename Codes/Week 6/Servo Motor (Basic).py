from machine import Pin,PWM
import time

p=PWM(Pin(4))    #Pin.OUT default hence optional
p.freq(50)

while True:
  p.duty(40)     #0 degree
  time.sleep(0.1)
  p.duty(77)     #90 degrees
  time.sleep(0.1)
