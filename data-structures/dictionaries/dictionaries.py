# Empty dictionary
empty = {}

# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values:

print(person["name"])      # Alice
print(person.get("age"))   # 30 (safer — returns None if key doesn't exist)

person["email"] = "alice@example.com"  # add new key
person["age"] = 31                     # update existing key

print(person)

# Loop through keys
for key in person:
    print(key)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Loop through just values
for value in person.values():
    print(value)

del person["city"]             # remove by key
removed = person.pop("email")  # remove and return the value

person.keys()       # all keys
person.values()     # all values
person.items()      # all (key, value) tuples
len(person)         # number of entries
"name" in person    # True — check if key exists


squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}