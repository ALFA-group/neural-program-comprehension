numbers = [1, 2, -2, -8, 0]
stride = 2
result = []

for idx in range(0, len(numbers), stride):
    result.append(numbers[idx] - 1)

print(result)

