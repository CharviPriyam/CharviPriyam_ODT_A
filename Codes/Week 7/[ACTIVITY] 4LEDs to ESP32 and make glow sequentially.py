from machine import Pin
import time
l1=Pin(12,Pin.OUT)
l2=Pin(14,Pin.OUT)
l3=Pin(27,Pin.OUT)
l4=Pin(26,Pin.OUT)
t=0.1

while True:
    #1st Second
    l1.value(1)
    l2.value(0)
    l3.value(0)
    l4.value(0)
    time.sleep(t)
    #2nd Second
    l1.value(0)
    l2.value(1)
    l3.value(0)
    l4.value(0)
    time.sleep(t)
    #3rd Second
    l1.value(0)
    l2.value(0)
    l3.value(1)
    l4.value(0)
    time.sleep(t)
    #4th Second
    l1.value(0)
    l2.value(0)
    l3.value(0)
    l4.value(1)
    time.sleep(t)
    
