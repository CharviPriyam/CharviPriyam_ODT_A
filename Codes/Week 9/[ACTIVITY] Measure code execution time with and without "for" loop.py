#Measure code execution time w/ and w/o "for" loop
import time
x=time.ticks_us()
print("Start time: ",x)

for i in range(1,11):
    print(i)
    time.sleep(1.5)
    i+=1
y=time.ticks_us()
print("End time: ",y)
print("Diff: ",time.ticks_diff(y,x))

z=time.ticks_us()
print("Start time w/o 'for': ",z)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
a=time.ticks_us()
print("End time w/o 'for': ",a)
print("Diff w/o 'for': ",time.ticks_diff(a,z))

