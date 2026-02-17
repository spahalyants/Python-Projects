# list comprehension

# "For each item in items, give me item[1],
#  and collect all those results into a new list."

items = [("a", 10), ("b", 9), ("c", 12)]

x = [item[1] for item in items]

print(x)



