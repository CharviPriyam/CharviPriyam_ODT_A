from machine import Pin
import time
l1=Pin(12,Pin.OUT) 
l2=Pin(14,Pin.OUT) 
l3=Pin(27,Pin.OUT) 
l4=Pin(26,Pin.OUT) 
p1=Pin(18,Pin.IN,Pin.PULL_UP)
p2=Pin(19,Pin.IN,Pin.PULL_UP)
while True:
  p1_val=p1.value()
  if p1_val==0:
    l1.off()
    time.sleep(0.2)
    l2.off()
    time.sleep(0.22)
    l3.off()
    time.sleep(0.24)
    l4.off()
    time.sleep(0.26)
    l4.on()
    time.sleep(0.28)
    l3.on()
    time.sleep(0.3)
    l2.on()
    time.sleep(0.32)
    l4.on()
    time.sleep(0.34)
    l1.off()
    l2.off()
    l3.off()
    l4.off()
  else:
    l1.on()
    l2.on()
    l3.on()
    l4.on()
  
  
