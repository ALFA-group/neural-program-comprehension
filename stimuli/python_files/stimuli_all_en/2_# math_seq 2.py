import math

a, b = 4, 8
mean = (a + b) / 2
variance = (a - mean)**2 + (b - mean)**2
dev = math.sqrt(variance / 2)

print(dev)

