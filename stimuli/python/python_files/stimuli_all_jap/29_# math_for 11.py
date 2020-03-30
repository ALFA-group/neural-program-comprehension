risto1 = [4, 4, 6]
risto2 = [1, 2, 4]
risto3 = [3, 2, 1]

for ai in range(len(risto1)):
    risto3[ai] += risto1[ai] + risto2[ai]

print(risto3)

