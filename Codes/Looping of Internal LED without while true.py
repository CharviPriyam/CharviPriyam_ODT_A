from machine import Pin
import time
l=Pin(2,Pin.OUT)
n=4
while (n>3):
  l.on()
  time.sleep(1)
  l.off()
  time.sleep(1)
#the point of this is to provide a condition that is ALWAYS true. Hence, the LED will keep blinking.
