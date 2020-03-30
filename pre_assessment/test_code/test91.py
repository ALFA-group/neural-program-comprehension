def who_won(a, b):
    if a == 10:
        return "a"
    if a < 10:
        return "b"
    if b == 10:
        return "b"
    if b < 10:
        return "a"
    if a == 10 and b == 10:
        return "tie"

print(who_won(10,10))