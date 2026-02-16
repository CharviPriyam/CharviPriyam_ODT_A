from machine import Pin
import time

pb=Pin(4,Pin.IN,Pin.PULL_UP)

while True:
  pv=pb.value()
  print(pv)
  time.sleep(0.2)

#output is 1, 0 when button is pushed
