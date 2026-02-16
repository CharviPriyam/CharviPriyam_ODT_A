from machine import Pin
import neopixel
import random
import time

l=[(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0)]
n=neopixel.NeoPixel(Pin(12),16)

while True:
	for i in range(0,16):
        x=random.randint(0,15)
    	n[i]=l[x]
    	time.sleep(0.1)
    	n.write()