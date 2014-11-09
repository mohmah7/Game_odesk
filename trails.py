import random

x = 2
y = 3

while x%y != 0:
    x = random.randrange(0,15)
    y = random.randrange(1,15)

print x,y