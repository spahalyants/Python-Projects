#1

my_list = [55, 'Samvel', 77.25, True, [10,1000]]

print(my_list)

#2

del(my_list[2])
print(my_list)

#3

print(len(my_list))

#4 --> 2 ways: first  - creates a new list,
#              second - modifies the original.

new_list = list(reversed(my_list))
print(new_list)

my_list.reverse()
print(my_list)

#5

third_list = ['apple', 'whale']
combined_list = my_list + third_list

print(combined_list)