import math

kazu1, kazu2, kazu3 = 10, 12, 14

if math.sqrt(kazu1 + kazu2 + kazu3).is_integer():
    print(kazu1 + kazu2 + kazu3)
else:
    print(kazu2 + kazu3)

