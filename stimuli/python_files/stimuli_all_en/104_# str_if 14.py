sentence = "I am a"
word = "cat"

if len(word) > 3:
    print(word)
elif sentence[-1] == word[1]:
    print(sentence)
else:
    print(sentence + " " + word)

