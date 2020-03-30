old = "stuff"
threshold = 2

if len(old) < 2:
    threshold = len(old)

new = old[:threshold]

print(new)

