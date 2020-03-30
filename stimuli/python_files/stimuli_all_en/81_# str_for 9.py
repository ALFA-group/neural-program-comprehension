animal = "pigs"
new_word = ""

for char in range(len(animal) - 1, -1, -2):
    new_word += animal[char]

print(new_word)

