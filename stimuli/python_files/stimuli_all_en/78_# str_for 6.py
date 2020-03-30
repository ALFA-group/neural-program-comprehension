word = "outer"
letters = "the"
classifier = []

for letter in letters:
    classifier.append(letter in word)

print(classifier)

