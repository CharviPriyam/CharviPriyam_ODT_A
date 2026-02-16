from machine import Pin
import neopixel
import time
l=[(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0)]
n=neopixel.NeoPixel(Pin(12),16)
for i in range(0,16):
    n[i]=l[x]
    time.sleep(0.1)
    n.write()
