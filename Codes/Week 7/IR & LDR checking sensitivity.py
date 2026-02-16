#IR and LDR sensor checking sensitivity

from machine import Pin
import time
s=Pin(4,Pin.IN,Pin.PULL_UP)
l=Pin(12,Pin.OUT)
while True:
    s_val=s.value()
    print(s_val)
    time.sleep(0.1)
    if s_val==0:
        l.on()
    else:
        l.off()
    
#clockwise tightening increases sensitivity
#IR just tells obstacle is present, Ultrasound sensor (HC-SR04) shows how FAR the sensor is. Works on concept of radar (echo).
# it measures distance by the constant ultrasound speed and time we provide (s*t).
#code is complicated, refer LMS
#We'll provide small pulse to trig pin (10 micro seconds pulse by using time.sleep) - it will then start generating ultrasound pulse when triggered.
#Then listen to echo - echo pin goes high when ultrasound leaves and it goes low when ultraound arrives - hence time is calculated.
#Hence, distance is calculated.
#trig and echo pin to GPIO
