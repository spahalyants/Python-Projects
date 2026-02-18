# Python’s “ternary condition” is called a conditional expression:

# value_if_true if condition else value_if_false


age = 20
status = "adult" if age >= 18 else "minor"

print(status)


# With a function call

is_valid = False
print("OK" if is_valid else "Not OK")


# Common pattern: fallback value

name = input("Name: ")
display = name if name else "Anonymous"

print(display)


# Nested (works, but can get hard to read)

x = 99
grade = "A" if x >= 90 else "B" if x >= 80 else "C"
