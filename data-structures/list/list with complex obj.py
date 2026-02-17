items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

def sort_item(item):
    return item[1]

# list is sorted by the price of each item

items.sort(key=sort_item)
print(items)

# a shorter way using lambda function:

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items.sort(key=lambda item: item[1])
print(items)