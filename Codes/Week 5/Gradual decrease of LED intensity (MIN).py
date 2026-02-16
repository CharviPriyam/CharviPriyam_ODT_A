from machine import Pin,PWM
import time
l=PWM(Pin(4))
l.freq(500)
while True:
  for i in range(1023,0,-1):
    l.duty(i)
    time.sleep(0.001)
