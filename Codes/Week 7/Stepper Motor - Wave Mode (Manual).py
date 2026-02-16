#Stepper motor

from machine import Pin
import time
l1=Pin(5,Pin.OUT)
l2=Pin(14,Pin.OUT)
l3=Pin(18,Pin.OUT)
l4=Pin(19,Pin.OUT)

while True:
    #1st Second
    l1.value(1)      #ms = milli second
    l2.value(0)      #us = micro second
    l3.value(0)
    l4.value(0)
    time.sleep_ms(5)
    #2nd Second
    l1.value(0)
    l2.value(1)
    l3.value(0)
    l4.value(0)
    time.sleep_ms(5)
    #3rd Second
    l1.value(0)
    l2.value(0)
    l3.value(1)
    l4.value(0)
    time.sleep_ms(5)
    #4th Second
    l1.value(0)
    l2.value(0)
    l3.value(0)
    l4.value(1)
    time.sleep_ms(5)
