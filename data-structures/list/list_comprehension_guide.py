[x**2 for x in range(10)] # Squares
[x for x in range(20) if x % 2 == 0] # Even numbers
[name.upper() for name in names] # Transform
['even' if x%2==0 else 'odd' for x in range(5)] # If-else


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = [n for row in matrix for n in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Эквивалент с обычными циклами:
flat = []

for row in matrix:       # внешний цикл
    for n in row:        # внутренний цикл
        flat.append(n)

