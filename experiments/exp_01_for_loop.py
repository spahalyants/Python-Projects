word = "trigonometry"

for i in range(len(word)):
    if i == len(word) - 1:
        print(word[i])
    else:
        print(word[i], end="--")


i = 0
for letter in word:
    if i == len(word) - 1:
        print(letter)
    else:
        print(letter, end="--")
    i += 1


for i, letter in enumerate(word):
    if i == len(word) - 1:
        print(letter)
    else:
        print(letter, end="--")