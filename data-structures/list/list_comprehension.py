# list comprehension

# "For each item in items, give me item[1],
#  and collect all those results into a new list."

items = [("a", 10), ("b", 9), ("c", 12)]

x = [item[1] for item in items]

print(x)     # [10, 9, 12]


items = [("a", 10), ("b", 9), ("c", 12)]

items.sort(key=lambda item: item[1])  # sort by price
print(items)

items.sort(key=lambda item: item[0])  # sort by product name
print(items)

