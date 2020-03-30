numbers = [4, 5, 3, 8, 3, 2, 5]
length = len(numbers)
answer = 0

for i in range(length // 2 + 1):
    answer += numbers[i]

print(answer)

