from machine import Pin
import time
l=Pin(2,Pin.OUT)
while True:
  l.on()
  time.sleep(1)
  l.off()
  time.sleep(1)
