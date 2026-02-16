from machine import Pin,TouchPad
import time
#set up touchpad
t=TouchPad(Pin(12))
while True:
  t_val=t.read()
  print(t_val)
  time.sleep(0.4) #provides value in 0.4 seconds interval
