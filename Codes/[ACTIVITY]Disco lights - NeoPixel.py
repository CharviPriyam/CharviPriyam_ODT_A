from machine import Pin
import time
import random
import neopixel

np=neopixel.NeoPixel(Pin(12),16)
t=TouchPad(Pin(4))

while True:
  tv=t.read()
  time.sleep(0.4)
  if tv<300:
    print("hi")
    for j in range(0,4,1):
      print(j)
      np[j]=(255,51,53)
      time.sleep(0.1)
      np.write()
    for k in range(4,8,1):
      print(k)
      np[k]=(51,0,255)
      time.sleep(0.1)
      np.write()
    for l in range(8,12,1):
      print(l)
      np[l]=(255,0,51)
      time.sleep(0.1)
      np.write()
    for m in range(12,16,1):
      print(m)
      np[m]=(0,255,255)
      time.sleep(0.1)
      np.write()
    for n in range(0,16,1):
      print(n)
      np[n]=(255,51,153)
      time.sleep(0.05)
      np.write()
    for o in range(0,16,1):
      print(o)
      np[o]=(51,0,255)
      time.sleep(0.05)
      np.write()
    for p in range(0,16,1):
      print(p)
      np[p]=(255,0,51)
      time.sleep(0.05)
      np.write()
    for q in range(0,16,1):
      print(q)
      np[q]=(0,255,255)
      time.sleep(0.05)
      np.write()
    print("Pin 4 us touched")
  else:
    for i in range(0,16,1):
      print(i)
      np[i]=(255,255,255)
      np.write()
      print("Not touched")
