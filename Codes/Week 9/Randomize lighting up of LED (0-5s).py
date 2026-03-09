from machine import Pin
import time
import random

l=Pin(12,Pin.OUT)

r=random.randrange(0,6)
l.off()
time.sleep(r)
l.on()
