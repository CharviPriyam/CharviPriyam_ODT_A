from machine import Pin
import random
import time

pb=Pin(4,Pin.IN,Pin.PULL_UP)

while True:
  pv=pb.value()
  if pv==0:
    r=random.randint(1,10)
    time.sleep(0.2)
    print(r)
  
