#time.time() time duration
import time
import random
x=time.time()
print(x)

while True:
    r=random.randrange(10)
    print(r)
    time.sleep(2)
    y=time.time()
    print(y)
    print(y-x)
