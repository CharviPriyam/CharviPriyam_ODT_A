#VCC to 3v3
#GND to GND (ESP32)
#DO to GPIO

from machine import Pin
import time
ldr=Pin(14,Pin.IN,Pin.PULL_UP)
while True:
  ldr_v=ldr.value()
  print(ldr_v)
  time.sleep(0.2)

#output is 0 in general, 1 when you cover with hand (no light)
