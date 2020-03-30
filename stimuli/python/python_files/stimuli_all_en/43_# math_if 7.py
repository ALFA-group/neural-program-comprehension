mine, yours, hers = 5, 3, 2

if yours < mine and mine < hers:
    print(mine)

elif hers < mine and mine < yours:
    print(mine)

elif hers < yours and yours < mine:
    print(yours)

elif mine < yours and yours < hers:
    print(yours)

else:
    print(hers)

