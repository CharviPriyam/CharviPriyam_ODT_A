from machine import Pin
import time
import neopixel

np=neopixel.NeoPixel(Pin(4),16)

np[0]=(255,0,0)
np[1]=(0,255,0)
np[2]=(0,0,255)
np[3]=(255,0,0)
np[4]=(0,255,0)
np[5]=(0,0,255)
np[6]=(255,0,0)
np[7]=(0,255,0)
np[8]=(0,0,255)
np[9]=(255,0,0)
np[10]=(0,255,0)
np[11]=(0,0,255)
np[12]=(255,0,0)
np[13]=(0,255,0)
np[14]=(0,0,255)
np[15]=(255,0,0)
np.write()
