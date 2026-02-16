fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# apple
# banana
# cherry


for i in range(5):
    print(f"i equals: {i}")
# 0, 1, 2, 3, 4

print()

for x in range(1,10,2):
    print(f"x equals: {x}")
# 1, 3, 5, 7, 9

print()

for char in "Samvel":
    print(char, end=" ")
# By default, print() uses end="\n" (newline).
# S a m v e l

print()

# No separator
for char in "Samvel":
    print(char, end="")

# Samvel

print()

# Comma separator
for char in "Samvel":
    print(char, end=", ")
# S, a, m, v, e, l,