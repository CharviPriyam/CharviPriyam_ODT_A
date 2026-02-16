from machine import Pin
import time
l=PWM(Pin(4))
l.freq(500)
l.duty(768)
