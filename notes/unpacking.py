# taking values from a collection and assigning them
# to individual variables in one step.

# Important Rule:
# The number of variables must match the number of values.

### Tuple/List Unpacking ###

# Instead of this:

point = (10, 20)
x = point[0]
y = point[1]

# You can do this:

x, y = (10, 20)
print(x)  # 10
print(y)  # 20

# Works with lists too:

a, b, c = [1, 2, 3]
print(a)  # 1
print(b)  # 2
print(c)  # 3


# If you don't know the exact count, use * to catch the rest:

first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5


# A common use for Swapping Variables — no temp variable needed:

a = 5
b = 10
a, b = b, a
print(a)  # 10
print(b)  # 5


# Unpacking in Loops

pairs = [(1, "apple"), (2, "banana"), (3, "cherry")]

for number, fruit in pairs:
    print(number, fruit)

# 1 apple
# 2 banana
# 3 cherry