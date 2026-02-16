from machine import Pin,TouchPad
import time

t=TouchPad(Pin(12))
l=Pin(2,Pin.OUT)

while True:
  t_val=t.read()
  print(t_val)
  time.sleep(0.4)
  if t_val<100:
    l.on()
    time.sleep(1)
    l.off()
    time.sleep(1)
