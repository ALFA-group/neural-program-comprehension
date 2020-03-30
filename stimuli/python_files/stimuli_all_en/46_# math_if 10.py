import math

num1, num2, num3 = 10, 12, 14

if math.sqrt(num1 + num2 + num3).is_integer():
    print(num1 + num2 + num3)
else:
    print(num2 + num3)

