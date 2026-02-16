from machine import Pin
import time

in1 = Pin(5, Pin.OUT)
in2 = Pin(14, Pin.OUT)
in3 = Pin(18, Pin.OUT)
in4 = Pin(19, Pin.OUT)

while True:
    for i in range(500):
        in1.value(1)
        in2.value(0)
        in3.value(0)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(0)
        in2.value(1)
        in3.value(0)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(0)
        in2.value(0)
        in3.value(1)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(0)
        in2.value(0)
        in3.value(0)
        in4.value(1)
        time.sleep_ms(5)
    time.sleep(1)
    
    for i in range(500):
        in1.value(0)
        in2.value(0)
        in3.value(0)
        in4.value(1)
        time.sleep_ms(5)
        
        in1.value(0)
        in2.value(0)
        in3.value(1)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(0)
        in2.value(1)
        in3.value(0)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(1)
        in2.value(0)
        in3.value(0)
        in4.value(0)
        time.sleep_ms(5)
    time.sleep(1)
    
#clock and anticlock manually
