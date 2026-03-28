from machine import Pin,ADC
import time

s=ADC(Pin(4))
s.ATTN_11DB 

while True:
    sval=s.read()
    print(sval)
    time.sleep(0.5)
