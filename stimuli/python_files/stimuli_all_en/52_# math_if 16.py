temperature = 70
humidity = 100

if temperature >= 100:
    print("A")
elif temperature >= 92 and humidity > 75:
    print("B")
elif temperature > 88 and humidity >= 85:
    print("C")
elif temperature == 75 and humidity <= 65:
    print("D")
else:
    print("E")

