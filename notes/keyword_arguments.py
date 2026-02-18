# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

for x in range(1, 11):
    print(x, end = " ")


# Here end = " " is a keyword argument passed to the print() function.
# By default, print() adds a newline (\n) at the end of each output.
# By setting end=" ", you're telling it to use a space instead of a newline.

# When defining a function, the order should be:
# def func(positional, default=value, *args, **kwargs)

print()

##########################################################

# These are the 4 types of arguments in Python:

# 1. Positional — order matters, matched by position:

def greet(name, age):
    print(f"{name} is {age}")

greet("Samvel", 25)  # name="Samvel", age=25
greet(25, "Samvel")  # name=25, age="Samvel" — wrong!


# 2. Default — has a default value, so it's optional when calling:

def greet(name, age=18):
    print(f"{name} is {age}")

greet("Samvel")      # age defaults to 18
greet("Samvel", 25)  # age = 25


# 3. Keyword — passed by name, so order doesn't matter:

def greet(name, age):
    print(f"{name} is {age}")

greet(age=25, name="Samvel")  # works perfectly


# 4. Arbitrary — accepts any number of arguments:

# *args — arbitrary positional (collected as a tuple):

def add(*nums):
    print(sum(nums))

add(1, 2, 3)      # 6
add(1, 2, 3, 4)   # 10


# **kwargs — arbitrary keyword (collected as a dictionary):

def info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

info(name="Samvel", age=25, city="Yerevan")
# name: Samvel
# age: 25
# city: Yerevan

##########################################################

# data.items() returns pairs (tuples) like:

data = {"name": "Samvel", "age": 25}
data.items()

# dict_items([("name", "Samvel"), ("age", 25)])

# Tuple Unpacking in dict.items()
# ================================
# Each item is a tuple of two elements:
#     ("name", "Samvel"), ("age", 25)
#
# When you write: for key, value in data.items()
#     Python sees two variables on the left
#     and a tuple of two elements on the right,
#     and simply unpacks:
#
#         first element  -> first variable  (key)
#         second element -> second variable (value)