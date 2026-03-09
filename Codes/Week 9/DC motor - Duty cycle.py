from machine import Pin,PWM
import time

IN1=Pin(12,Pin.OUT)
IN2=Pin(13,Pin.OUT)
ENA=PWM(Pin(15,Pin.OUT))
ENA.freq(1000)

while True:
    IN1.value(1)
    IN2.value(0)
    time.sleep(3)
    ENA.duty(1000)
    IN1.value(0)
    IN2.value(1)
    time.sleep(3)
    ENA.duty(512)
