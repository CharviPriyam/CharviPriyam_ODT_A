from machine import Pin
import neopixel
import random
import time

n=neopixel.NeoPixel(Pin(12),16)

while True:
    
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    r1=random.randint(0,255)
    g1=random.randint(0,255)
    b1=random.randint(0,255)
    r2=random.randint(0,255)
    g2=random.randint(0,255)
    b2=random.randint(0,255)
    r3=random.randint(0,255)
    g3=random.randint(0,255)
    b3=random.randint(0,255)
	for i in range(0,4):
    	n[i]=(r,g,b)
        print(r,g,b)
    	time.sleep(0.1)
    	n.write()
    for j in range(4,8):
    	n[j]=(r1,g1,b1)
        print(r1,g1,b1)
    	time.sleep(0.1)
    	n.write()
    for k in range(8,12):
    	n[k]=(r2,g2,b2)
        print(r2,g2,b2)
    	time.sleep(0.1)
    	n.write()
    for l in range(12,16):
    	n[l]=(r3,g3,b3)
        print(r3,g3,b3)
    	time.sleep(0.1)
    	n.write()
