letters = ["a", "b", "c"]

if "d" in letters:
    print(letters.index("b"))

numbers = [3, 51, 2, 8, 6]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers = [3, 51, 2, 8, 6]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

