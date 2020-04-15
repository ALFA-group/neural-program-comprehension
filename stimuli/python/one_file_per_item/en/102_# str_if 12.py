letters = ["a", "e", "t", "o", "u"]
word = "CreepyNuts"

if (word[1] in letters) and (word[6] in letters):
    print(0)
elif (word[1] in letters) or (word[6] in letters):
    print(1)
else:
    print(2)

