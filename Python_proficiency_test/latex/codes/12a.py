word = input("Enter two words (space separated): ")
word1 = word
number = len(word)
space = '/'  
for i in range(number):
    if(word1[i] == " "):
        word1[i] = space
print(word1)