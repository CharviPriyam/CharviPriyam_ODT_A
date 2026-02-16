from machine import Pin
import time
import neopixel

np=neopixel.NeoPixel(Pin(12),16)
pb=Pin(4,Pin.IN,Pin.PULL_UP)

while True:
  val=pb.value()
  if val==0:
    for i in range(16):
      val=pb.value()
      if val==0:
        break
      np[i]=(255,0,0)
      np.write()
      time.sleep(2)
    time.sleep(0.2)

#"If" is a CONDITIONAL STATEMENT, it is NOT a loop, here, "break" only breaks the flow of LOOPS. Hence, it breaks the "for" loop.
