nums = [1, 2, 3, 4, 5]
nums[0] # 1
nums[-1] # 5
nums[1:3] # [2, 3]
len(nums) # 5
3 in nums # True
# Methods
nums.append(6) # Add to end
nums.insert(0, 0) # Insert at index
nums.extend([7, 8]) # Add multiple
nums.remove(3) # Remove by value
nums.pop() # Remove last
nums.pop(0) # Remove by index
nums.sort() # Sort in place
nums.reverse() # Reverse in place
nums.index(4) # Find index
nums.count(2) # Count occurrences

# Sorted (new list, original unchanged)
sorted_nums = sorted(nums)

words = ["banana", "pie", "apple", "hi"]
sorted(words, key=len)

# ["hi", "pie", "apple", "banana"]


users = [
    {"name": "Charlie", "age": 30},
    {"name": "Alice",   "age": 22},
    {"name": "Bob",     "age": 27},
]

sorted(users, key=lambda u: u['age'])

# [{'name': 'Charlie', 'age': 30}, {'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 27}]
