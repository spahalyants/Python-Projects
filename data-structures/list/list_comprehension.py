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

#############################################

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

### map & filter vs list comprehension --> same result

prices_map_fn = list(map(lambda item: item[1], items))
prices_ls_comp_map = [item[1] for item in items]

print(prices_map_fn)
print(prices_ls_comp_map)

filtered_filt_fn = list(filter(lambda item: item[1] >= 10, items))
filtered_ls_comp = [item for item in items if item[1] >= 10]

print(filtered_filt_fn)
print(filtered_ls_comp)
