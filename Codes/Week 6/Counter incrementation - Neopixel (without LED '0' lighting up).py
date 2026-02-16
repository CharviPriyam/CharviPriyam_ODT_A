#LED no. 0 did not light up coz of increment
from machine import Pin
import time
import neopixel

n=neopixel.NeoPixel(Pin(12),16)
s=Pin(4,Pin.IN,Pin.PULL_UP)
i=-1

while True:
  s_val=s.value()
  if s_val==0:
    i+=1
    time.sleep(0.5)
    print(i)
    n[i]=(255,0,0)
    time.sleep(0.1)
    n.write()
  
    
