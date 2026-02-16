from machine import Pin
import time
c=0
s=Pin(4,Pin.IN,Pin.PULL_UP)

while True:
  s_val=s.value()
  if s_val==0:
    c+=1
    print(c)
    time.sleep(0.5)
    if c==5:
      c=0
      print(c)
