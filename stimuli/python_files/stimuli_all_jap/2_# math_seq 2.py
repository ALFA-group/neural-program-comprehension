import math

ei, be = 4, 8
heikin = (ei + be) / 2
bunsan = (ei - heikin)**2 + (be - heikin)**2
hensa = math.sqrt(bunsan / 2)

print(hensa)

