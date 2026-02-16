from machine import Pin
import time
l1=Pin(12,Pin.OUT)
l2=Pin(14,Pin.OUT)
l3=Pin(27,Pin.OUT)
l4=Pin(26,Pin.OUT)

while True:
    #1st Second
    l1.on()
    l2.off()
    l3.off()
    l4.off()
    time.sleep(1)
    #2nd Second
    l1.off()
    l2.on()
    l3.off()
    l4.off()
    time.sleep(1)
    #3rd Second
    l1.off()
    l2.off()
    l3.on()
    l4.off()
    time.sleep(1)
    #4th Second
    l1.off()
    l2.off()
    l3.off()
    l4.on()
    time.sleep(1)
