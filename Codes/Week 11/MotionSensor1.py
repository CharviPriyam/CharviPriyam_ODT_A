from machine import Pin
import time

s=Pin(14,Pin.IN)

print("Sensor Initialisation")
time.sleep(60)

while True:
    sval=s.value()
    print(sval)
    time.sleep(2)
    if sval ==1:
        print("Motion is detected")
