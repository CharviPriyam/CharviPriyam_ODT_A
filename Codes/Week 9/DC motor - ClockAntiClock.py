from machine import Pin
import time
IN1=Pin(12,Pin.OUT)
IN2=Pin(13,Pin.OUT)

while True:
    IN1.value(1)
    IN2.value(0)
    time.sleep(3)
    IN1.value(0)
    IN2.value(1)
    time.sleep(3)

