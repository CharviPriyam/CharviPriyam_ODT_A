#servo motor
from machine import Pin
import time
l1=Pin(5,Pin.OUT)
l2=Pin(14,Pin.OUT)
l3=Pin(18,Pin.OUT)
l4=Pin(19,Pin.OUT)

l=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
s=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

while True:
    for x in range(500):
        for i in l:
            l1.value(i[0])
            l2.value(i[1])
            l3.value(i[2])
            l4.value(i[3])
            time.sleep_ms(5) #5 milli seconds
    for x in range(500):
        for j in s:
            l1.value(j[0])
            l2.value(j[1])
            l3.value(j[2])
            l4.value(j[3])
            time.sleep_ms(5)
        
#shorter code 
#clock and anticlock using 2 lists
