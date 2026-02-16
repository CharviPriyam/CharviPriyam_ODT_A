from machine import Pin
import time
l=Pin(12,Pin.OUT) #12 being pin on board
while True:
  l.on()
  time.sleep(0.25)
  l.off()
  time.sleep(0.25)
  l.on()
  time.sleep(1)
  l.off()
  time.sleep(1)
