#time.ticks_ms() time duration
import time
import random

x=time.ticks_ms()
print(x)

r=random.randrange(10)
print(r)
time.sleep(2)
y=time.ticks_ms()
print(y)
print(y-x)
