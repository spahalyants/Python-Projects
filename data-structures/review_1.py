# list comprehension = list construction

# general syntax:
# [expression for item in iterable if condition]

# expression — what to put in the new list (can transform item)
# for item in iterable — the loop
# if condition — optional filter

list_sample = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16, 25]

even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]