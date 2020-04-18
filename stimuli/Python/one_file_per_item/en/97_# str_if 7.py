address = "https://www.mit.edu/bcs"

if address[0] == "h" and address[-1] == "/":
    print(address[1])
elif address[0] == "h":
    print(address[-1])
else:
    print(address)

