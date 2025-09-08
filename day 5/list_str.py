# Convert a list into a string:

list1 = ['a', 'b', 'c', '1', '2', '3']
my_str = ''.join(list1)
print(f'str = {my_str}')

# Convert a string into a list:
list2 = [element for element in my_str] # list comprehension
print(f'List = {list2}')