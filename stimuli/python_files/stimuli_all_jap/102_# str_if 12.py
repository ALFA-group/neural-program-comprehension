tegamis = ["a", "e", "t", "o", "u"]
gengo = "CreepyNuts"

if (gengo[1] in tegamis) and (gengo[6] in tegamis):
    print(0)
elif (gengo[1] in tegamis) or (gengo[6] in tegamis):
    print(1)
else:
    print(2)

