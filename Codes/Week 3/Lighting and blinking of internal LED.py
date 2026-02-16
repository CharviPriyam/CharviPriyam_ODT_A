from machine import Pin
import time
l=Pin(2,Pin.OUT)
l.on()
time.sleep(1)
l.off()
