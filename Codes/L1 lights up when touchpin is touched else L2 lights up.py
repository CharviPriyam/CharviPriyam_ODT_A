from machine import Pin,TouchPad
import time

t=TouchPad(Pin(12))
l1=Pin(12,Pin.OUT)
l2=Pin(12,Pin.OUT)

while True:
  tv=t.read()
  time.sleep(0.4)
  if tv<300:
    print("Pin 4 is touched")
    l1.on()
    time.sleep(1)
    l1.off()
  else:
    print("Not Touched")
    l2.on()
    time.sleep(1)
    l2.off()
  print(tv)
