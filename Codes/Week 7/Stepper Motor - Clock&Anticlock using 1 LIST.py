#servo motor
from machine import Pin
import time
l1=Pin(5,Pin.OUT)
l2=Pin(14,Pin.OUT)
l3=Pin(18,Pin.OUT)
l4=Pin(19,Pin.OUT)

l=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for x in range(500):
        for i in l:
            l1.value(i[0])
            l2.value(i[1])
            l3.value(i[2])
            l4.value(i[3])
            time.sleep_ms(3) #5 milli seconds
    for y in range(500):
        for k in l:
            l1.value(k[3])
            l2.value(k[2])
            l3.value(k[1])
            l4.value(k[0])
            time.sleep_ms(3)
        
#shorter code
#clock and anticlock using 1 list




