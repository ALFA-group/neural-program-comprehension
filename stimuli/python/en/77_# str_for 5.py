puzzle = "crow"
word_bank = []

for i in range(len(puzzle) - 1):
    word_bank.append(puzzle[i] + puzzle[i + 1])

print(word_bank)

