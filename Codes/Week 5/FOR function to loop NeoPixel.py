from machine import Pin
import time
import neopixel

np=neopixel.NeoPixel(Pin(12),16)

while True:
  for i in range(0,16,1):
    print(i)
    np[i]=(255,0,0)
    time.sleep(0.25)
    np.write()
    np[i+1]=(0,255,0)
    time.sleep(0.25)
    np.write()
