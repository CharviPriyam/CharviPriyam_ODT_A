from machine import Pin,PWM
import time

p=PWM(Pin(4))    #Pin.OUT default hence optional
p.freq(50)

while True:
  for i in range(0,120,1):
    p.duty(i)
    time.sleep(0.01)
  for j in range(120,-1,-1):
    p.duty(j)
    time.sleep(0.01)

