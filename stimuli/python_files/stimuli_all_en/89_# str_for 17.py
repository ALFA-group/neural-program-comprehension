piece1 = "gab"
piece2 = "cab"
answer = []

for ind in range(len(piece1)):
    answer.append(piece1[ind] == piece2[ind])

print(answer)

